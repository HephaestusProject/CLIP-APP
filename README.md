# CLIP-APP

### prerequisite

```sh
git clone --recursive https://github.com/HephaestusProject/CLIP-APP.git
pip install -r server/requirements.txt
```

### server

```sh
PYTHONPATH=.:./server/CLIP python server/app.py
```

### client

```sh
curl -X POST -H "Content-Type: application/json" 127.0.0.1:5000/pred/custom -d "{\"image_path\": \"CLIP.png\", \"texts\": [\"a diagram\", \"a dog\", \"a cat\"]}"
```
