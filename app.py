import os
import subprocess
import tempfile
import time

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run_command", methods=["POST"])
def run_command():
    try:
        # Create a shell script with the provided commands
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".sh", delete=False
        ) as script_file:
            script_path = script_file.name
            script_file.write(
                """#!/bin/bash
output_files=()
for i in $(seq -f "%02g" 1 12); do 
  node="ucsc-vlaa-$i"
  temp_file=$(mktemp)
  output_files+=($temp_file)

  (echo "=== $node ===" > $temp_file; ssh -o "StrictHostKeyChecking no" $node /data1/xhuan192/misc/miniconda3/bin/gpustat >> $temp_file) &
  sleep 0.5
done
wait
cat "${output_files[@]}"
rm "${output_files[@]}"
"""
            )

        # Make the script executable
        os.chmod(script_path, 0o755)

        # Run the shell script and capture output
        result = subprocess.run([script_path], capture_output=True, text=True)

        # Clean up the temporary script file
        os.unlink(script_path)

        # Return the output
        return jsonify(
            {"success": True, "output": result.stdout, "error": result.stderr}
        )
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
