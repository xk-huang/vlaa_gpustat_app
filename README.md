# vlaa_gpustat_app

install `gpustat` on each node.

make sure you can ssh each node.

Edit `  node="ucsc-vlaa-$i"` and `  (echo "=== $node ===" > $temp_file; ssh $node /data1/xhuan192/misc/miniconda3/bin/gpustat >> $temp_file) &` in `app.py` according to the gpustat path and node ssh hostname.

install `flask`

run the app `python app.py`