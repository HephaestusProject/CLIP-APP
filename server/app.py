import torch
import clip
import json
from PIL import Image

from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)


@app.route("/pred/<dataset>/<subpath>", methods=['POST'])
@cross_origin()
def get_gen(dataset, subpath):
    image = preprocess(Image.open('server/CLIP/' + subpath)).unsqueeze(0).to(device)
    # to be fixed
    text = ["a diagram", "a dog", "a cat"]
    text_encoded = clip.tokenize(text).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text_encoded)

        logits_per_image, logits_per_text = model(image, text_encoded)
        probs = logits_per_image.softmax(dim=-1).cpu().numpy()
        # 1 batch
        res = {key:value.tolist() for key, value in zip(text, probs[0])}

    return {'result': res}


if __name__ == '__main__':
    app.run()