import time

from flask import Flask, request

from openai_gateway import get_image_prompt, get_audio_prompt
from server.youtube_gateway import find_video

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/get_music", methods=["POST"])
async def get_audio():
    # mood_word = await get_audio_prompt(request.json["prompt"])
    # return await find_video(mood_word)

    # We don't have parts of the program connected properly so we have to hardcode this section
    time.sleep(3)
    return "https://www.youtube.com/watch?v=D7vrXDiKbEU"


@app.route("/api/get_video", methods=['POST'])
async def get_prompt():
    prompt = request.json['prompt']
    style = request.json['style']

    # return await create_image([get_image_prompt(prompt, style)])

    time.sleep(3)
    return [
        {
            "video": ('video1.mp4', open('files/video1.mp4', 'rb')),
            "audio": ('audio1.mp4', open('files/audio1.mp4', 'rb')),
            "thumbnail": ('thumbnail1.png', open('files/thumbnail1.png', 'rb')),
            "chunk": "Once upon a time there were three little pigs. One pig built a house of straw while the second pig built his house with sticks."
        },
        {
            "video": ('video2.mp4', open('files/video2.mp4', 'rb')),
            "audio": ('audio2.mp4', open('files/audio2.mp4', 'rb')),
            "thumbnail": ('thumbnail1.png', open('files/thumbnail2.png', 'rb')),
            "chunk": "They built their houses very quickly and then sang and danced all day because they were lazy. The third little pig worked hard all day and built his house with bricks."
        },
        {
            "video": ('video3.mp4', open('files/video3.mp4', 'rb')),
            "audio": ('audio3.mp4', open('files/audio3.mp4', 'rb')),
            "thumbnail": ('thumbnail1.png', open('files/thumbnail3.png', 'rb')),
            "chunk": "A big bad wolf saw the two little pigs while they danced and played and thought, “What juicy tender meals they will make!”"
        },
        {
            "video": ('video4.mp4', open('files/video4.mp4', 'rb')),
            "audio": ('audio4.mp4', open('files/audio4.mp4', 'rb')),
            "thumbnail": ('thumbnail1.png', open('files/thumbnail4.png', 'rb')),
            "chunk": "He chased the two pigs and they ran and hid in their houses. The big bad wolf went to the first house and huffed and puffed and blew the house down in minutes. The frightened little pig ran to the second pig’s house that was made of sticks. "
        },
        {
            "video": ('video5.mp4', open('files/video5.mp4', 'rb')),
            "audio": ('audio5.mp4', open('files/audio5.mp4', 'rb')),
            "thumbnail": ('thumbnail1.png', open('files/thumbnail5.png', 'rb')),
            "chunk": "The big bad wolf now came to this house and huffed and puffed and blew the house down in hardly any time. Now, the two little pigs were terrified and ran to the third pig’s house that was made of bricks."
        },
        {
            "video": ('video6.mp4', open('files/video6.mp4', 'rb')),
            "audio": ('audio6.mp4', open('files/audio6.mp4', 'rb')),
            "thumbnail": ('thumbnail1.png', open('files/thumbnail6.png', 'rb')),
            "chunk": "The big bad wolf tried to huff and puff and blow the house down, but he could not. He kept trying for hours but the house was very strong and the little pigs were safe inside. He tried to enter through the chimney but the third little pig boiled a big pot of water and kept it below the chimney. The wolf fell into it and died."
        },
        {
            "video": ('video7.mp4', open('files/video7.mp4', 'rb')),
            "audio": ('audio7.mp4', open('files/audio7.mp4', 'rb')),
            "thumbnail": ('thumbnail1.png', open('files/thumbnail7.png', 'rb')),
            "chunk": "The two little pigs now felt sorry for having been so lazy. They too built their houses with bricks and lived happily ever after."
        }
    ]




if __name__ == "__main__":
    app.run()
