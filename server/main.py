from flask import Flask, request

from openai_gateway import get_image_prompt, get_audio_prompt, get_summary
# from banana_gateway import create_image
# from youtube_gateway import find_video

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


# @app.route("/api/get_audio", methods=["POST"])
# async def get_audio():
#     mood_word = await get_audio_prompt(request.json["prompt"])
#     return await find_video(mood_word)


# @app.route("/api/get_video", methods=['POST'])
# async def get_prompt():
#     prompt = request.json['prompt']
#     style = request.json['style']

#     return await create_image([get_image_prompt(prompt, style)])


@app.route("/chunk_and_prompt", methods=['POST'])
def chunk_and_prompt():
    res = []
    prompt = request.json['prompt']
    counter = 0
    current_chunk = ""
    i = 0
    while i < len(prompt):
        letter = prompt[i]
        current_chunk += letter
        if (letter == '!' or letter == '.' or letter == '?'):
            while(prompt[i] == '!' or prompt[i] == '.' or prompt[i] == '?'):
                i += 1
            counter += 1
            if (counter == 1):
                print(f"chunked...{letter}...{i}")
                res.append(current_chunk)
                current_chunk = ""
                counter = 0
        i += 1

    res.append(current_chunk)
    for i in range(len(res)):
        res[i] = get_image_prompt(res[i], "cartoon")

    return res


if __name__ == "__main__":
    app.run()
