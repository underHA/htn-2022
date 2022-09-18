import time

from flask import Flask, request
from flask_cors import cross_origin

from openai_gateway import get_image_prompt, get_audio_prompt
from server.youtube_gateway import find_video

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/get_music", methods=["POST"])
@cross_origin()
def get_audio():
    # mood_word = await get_audio_prompt(request.json["prompt"])
    # return await find_video(mood_word)

    # We don't have parts of the program connected properly so we have to hardcode this section
    time.sleep(3)
    return "https://www.youtube.com/watch?v=D7vrXDiKbEU"


@app.route("/api/get_video", methods=['POST'])
@cross_origin()
def get_prompt():
    text = request.json['text']
    style = request.json['style']

    # return await create_image([get_image_prompt(prompt, style)])

    time.sleep(3)
    return [
        {
            "video": ('video1.mp4', "https://htn-bucket.s3.us-east-2.amazonaws.com/video1.mp4"),
            "audio": ('audio1.mp4', "https://cdn.discordapp.com/attachments/906430804756955150/1021033568341864469/audio1.wav"),
            "thumbnail": ('thumbnail1.png', "https://cdn.discordapp.com/attachments/906430804756955150/1021033594384302150/thumbnail1.png"),
            "chunk": "Once upon a time there were three little pigs. One pig built a house of straw while the second pig built his house with sticks."
        },
        {
            "video": ('video2.mp4', "https://htn-bucket.s3.us-east-2.amazonaws.com/video2.mp4"),
            "audio": ('audio2.mp4', "https://cdn.discordapp.com/attachments/906430804756955150/1021033568757108817/audio2.wav"),
            "thumbnail": ('thumbnail1.png', "https://cdn.discordapp.com/attachments/906430804756955150/1021033594791145472/thumbnail2.png"),
            "chunk": "They built their houses very quickly and then sang and danced all day because they were lazy. The third little pig worked hard all day and built his house with bricks."
        },
        {
            "video": ('video3.mp4', "https://htn-bucket.s3.us-east-2.amazonaws.com/video3.mp4"),
            "audio": ('audio3.mp4', "https://cdn.discordapp.com/attachments/906430804756955150/1021033569105227866/audio3.wav"),
            "thumbnail": ('thumbnail1.png', "https://cdn.discordapp.com/attachments/906430804756955150/1021033595218972702/thumbnail3.png"),
            "chunk": "A big bad wolf saw the two little pigs while they danced and played and thought, “What juicy tender meals they will make!”"
        },
        {
            "video": ('video4.mp4', "https://htn-bucket.s3.us-east-2.amazonaws.com/video4.mp4"),
            "audio": ('audio4.mp4', "https://cdn.discordapp.com/attachments/906430804756955150/1021033569608552458/audio4.wav"),
            "thumbnail": ('thumbnail1.png', "https://cdn.discordapp.com/attachments/906430804756955150/1021033595655176242/thumbnail4.png"),
            "chunk": "He chased the two pigs and they ran and hid in their houses. The big bad wolf went to the first house and huffed and puffed and blew the house down in minutes. The frightened little pig ran to the second pig’s house that was made of sticks. "
        },
        {
            "video": ('video5.mp4', "https://htn-bucket.s3.us-east-2.amazonaws.com/video5.mp4"),
            "audio": ('audio5.mp4', "https://cdn.discordapp.com/attachments/906430804756955150/1021033569893748836/audio5.wav"),
            "thumbnail": ('thumbnail1.png', "https://cdn.discordapp.com/attachments/906430804756955150/1021033596158480504/thumbnail5.png"),
            "chunk": "The big bad wolf now came to this house and huffed and puffed and blew the house down in hardly any time. Now, the two little pigs were terrified and ran to the third pig’s house that was made of bricks."
        },
        {
            "video": ('video6.mp4', "https://htn-bucket.s3.us-east-2.amazonaws.com/video6.mp4"),
            "audio": ('audio6.mp4', "https://cdn.discordapp.com/attachments/906430804756955150/1021033570229301339/audio6.wav"),
            "thumbnail": ('thumbnail1.png', "https://cdn.discordapp.com/attachments/906430804756955150/1021033596586311760/thumbnail6.png"),
            "chunk": "The big bad wolf tried to huff and puff and blow the house down, but he could not. He kept trying for hours but the house was very strong and the little pigs were safe inside. He tried to enter through the chimney but the third little pig boiled a big pot of water and kept it below the chimney. The wolf fell into it and died."
        },
        {
            "video": ('video7.mp4', "https://htn-bucket.s3.us-east-2.amazonaws.com/video7.mp4"),
            "audio": ('audio7.mp4', "https://cdn.discordapp.com/attachments/906430804756955150/1021033570745208893/audio7.wav"),
            "thumbnail": ('thumbnail1.png', "https://cdn.discordapp.com/attachments/906430804756955150/1021033597219643443/thumbnail7.png"),
            "chunk": "The two little pigs now felt sorry for having been so lazy. They too built their houses with bricks and lived happily ever after."
        }
    ]




if __name__ == "__main__":
    app.run()
