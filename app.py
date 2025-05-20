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
        # Make the script executable
        script_path = "./gpuview_script.sh"
        os.chmod(script_path, 0o755)

        # Run the shell script and capture output
        result = subprocess.run([script_path], capture_output=True, text=True)

        # Return the output
        return jsonify(
            {"success": True, "output": result.stdout, "error": result.stderr}
        )
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
