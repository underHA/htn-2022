import asyncio

from flask import Flask, request

from openai_gateway import get_image_prompt
from server.banana_gateway import create_image

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/get_video", methods=['POST'])
def get_prompt():
    prompt = request.json['prompt']

    create_image([get_image_prompt(prompt)])





if __name__ == "__main__":
    app.run()
