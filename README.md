# vlaa_gpustat_app

How to setup locally.

make sure you can ssh each node. Edit `custom_ssh_config` accordingly, including `Hostname`, `User`, etc. And then try:
```
ssh -F ./custom_ssh_config vlaa-01.be.ucsc.edu
```

Install `gpustat` on each node.

Search all the `gpustat_path=` in `gpuview_script.sh`, change it to your own path.


Install `flask`

run the app `python app.py`

Then forward the port
```bash
ssh -L 5000:localhost:5000 $ssh_alias
```

Visit `localhost:5000` in your browser.