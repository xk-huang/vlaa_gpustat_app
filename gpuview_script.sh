#!/bin/bash

# VLAA
gpustat_path="/data1/xhuan192/misc/miniconda3/bin/gpustat"
output_files=()

for i in $(seq -f "%02g" 1 12); do 
  node="ucsc-vlaa-$i"
  temp_file=$(mktemp)
  output_files+=($temp_file)

  (
    echo "=== $node ===" > $temp_file
    if ! timeout 5 ssh -F ./custom_ssh_config $node $gpustat_path >> $temp_file 2>&1; then
      echo "[ERROR] Timeout or command failed on $node" >> $temp_file
    fi
  ) &
  sleep 0.5
done
wait
cat "${output_files[@]}"
rm "${output_files[@]}"

# AWS
gpustat_path="gpustat"
output_files=()
for i in $(seq 0 1 7); do 
  node="aws-64-l40s-$i"
  temp_file=$(mktemp)
  output_files+=($temp_file)

  (
    echo "=== $node ===" > $temp_file
    if ! timeout 5 ssh -F ./custom_ssh_config $node $gpustat_path >> $temp_file 2>&1; then
      echo "[ERROR] Timeout or command failed on $node" >> $temp_file
    fi
  ) &
  sleep 0.5
done
wait
cat "${output_files[@]}"
rm "${output_files[@]}"