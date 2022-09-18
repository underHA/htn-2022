from flask import Flask, request

from openai_gateway import get_image_prompt, get_audio_prompt
from server.banana_gateway import create_image
from server.youtube_gateway import find_video

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/get_audio", methods=["POST"])
async def get_audio():
    mood_word = await get_audio_prompt(request.json["prompt"])
    return await find_video(mood_word)


@app.route("/api/get_video", methods=['POST'])
async def get_prompt():
    prompt = request.json['prompt']
    style = request.json['style']

    return await create_image([get_image_prompt(prompt, style)])


if __name__ == "__main__":
    app.run()
