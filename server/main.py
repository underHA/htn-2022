from flask import Flask, request

from openai_gateway import get_image_prompt

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/get_video", methods=['POST'])
def get_prompt():
    prompt = request.json['prompt']





if __name__ == "__main__":
    app.run()
