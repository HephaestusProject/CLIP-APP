# CLIP-APP

### prerequisite

```sh
pip install -r server/requirements.txt
```

### server

```sh
PYTHONPATH=.:./server/CLIP python server/app.py
```

### client

```sh
curl -X POST 127.0.0.1:5000/pred/custom/CLIP.png
```
