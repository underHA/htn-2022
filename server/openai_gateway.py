import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def send_to_openai_completion(text: str, max_tokens: int = 150):
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        temperature=1,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=['\n']
    )
    return response.choices[0].text


image_prompt_types = {
    "photorealistic": "{insert_prompt},muscle extremely detailed, face, trending on artstation, pixiv, cgsociety, hyperdetailed Unreal Engine, optimization 4k 8k ultra HD, WLOP",

    "surrealist": "{insert_prompt} by greg rutkowski, ultradetailed digital painting, 8 k, realism, intriguing",

    "pastel": "{insert_prompt}, depressed mood, in the style of artgerm, gerald brom, atey ghailan and mike mignola, vibrant colors and hard shadows and strong rim light, plain background, comic cover art, trending on artstation",

    "psychedelic": "a painting of many synthwave colors and {insert_prompt}, an ultrafine detailed painting by unkoku togan, pixiv contest winner, space art, cosmic horror, lovecraftian, psychedelic ",

    "cinematic": "realistic screenshot from blade runner movie of {insert_prompt} intricate, moody lighting, highly detailed, cinematic, photoreal octane rendering, denis villeneuve, craig mullins, ridley scott ",

    "dreamy": "{insert_prompt}, trending on Artstation, painting by Jules Julien, Leslie David and Lisa Frank and Peter Mohrbacher and Alena Aenami and Dave LaChapelle muted colors with minimalism",

    "fable": "{insert_prompt} in the Style of Atey Ghailan and Mike Mignola and Artgerm, vibrant colors, hard shadows,  Comic Cover Art, trending on artstation",

    "anime": "soft studio lighting delicate features finely detailed {insert_prompt}, trending on pixiv fanbox, illustrated by greg rutkowski makoto shinkai takashi takeuchi studio ghibli",

    "cartoon": "{insert_prompt}, graduation album cover color palette : : by martine johanna and simon stalenhag and chie yoshii and casey weldon and wlop : : ornate, dynamic, particulate, rich colors, intricate, elegant, highly detailed, vogue, harper's bazaar art, fashion magazine, smooth, sharp focus, 8 k, octane render, ",

    "comic book": "a comic book style illustration of {insert_prompt} by moebius and makoto shinkai and rossdraws, ornate, lights, cosmic, featured on artstation, pixiv, volumetric lighting, 8 k, highly detailed render, octane render, unreal engine, soft glow, crisp lines, f 1 1, sharp focus, "

}


def _make_image_prompt(prompt: str):
    return "Q: What is CLIP+Diffusion AI Art Generation?" \
           "A: CLIP+Diffusion AI Art Generation is a method of creating art using artificial intelligence. This method involves using a neural network to generate images, and then using a diffusion process to create variations on those images." \
           "" \
           "Q: How should you write the text prompt for a art generation software to get ideal output for character art?" \
           "A: You should write a descriptive prompt that clearly identifies the subject, objects in the scene, and the background, using short, descriptive words which are separated by commas." \
           "" \
           "Q: Here are some example prompts:" \
           "A: The second coming of smaug, by dan mumford, yusuke murata, makoto shinkai, ross tran, cosmic, heavenly, god rays, intricate detail, cinematic, 8 k, cel shaded, unreal engine, featured on artstation, pixiv" \
           "" \
           "A: portrait of a young ruggedly handsome but joyful pirate, male, masculine, full body, red hair, long hair, d & d, fantasy, intricate, elegant, highly detailed, digital painting, artstation, concept art, matte, sharp focus, illustration, art by alphonse mucha" \
           "" \
           "A: a highly detailed epic cinematic concept art CG render digital painting artwork: Interstellar . By Greg Rutkowski, in the style of Francis Bacon and Syd Mead and Norman Rockwell and Beksinski, open ceiling, highly detailed, painted by Francis Bacon and Edward Hopper, painted by James Gilleard, surrealism, airbrush, Ilya Kuvshinov, WLOP, Stanley Artgerm, very coherent, triadic color scheme, art by Takato Yamamoto and James Jean" \
           "" \
           f"Q: Write a comma separated text prompt for a AI art generation software that would best describe the scene from the following sentence: \"{prompt}\"." \
           "A:"


def _make_audio_prompt(prompt: str):
    return f"Read the following passage: \"{prompt}\"." \
           "" \
           "The mood of the passage is very"


def get_image_prompt(prompt: str, style: str):
    return image_prompt_types[style].format(insert_prompt=send_to_openai_completion(_make_image_prompt(prompt)))


forbidden_words = {'there', 'well', 'defined', 'tone', 'ain', 'all', 'and', 'and', 'any', 'are', 'are', 'but', 'can', 'can', 'did', 'did', 'don', 'few', 'for', 'had', 'had', 'has', 'has', 'her', 'him', 'his', 'how', 'isn', 'its', 'may', 'nor', 'not', 'now', 'our', 'own', 'she', 'the', 'the', 'too', 'was', 'was', 'who', 'why', 'won', 'you', 'aren', 'been', 'been', 'both', 'dare', 'didn', 'does', 'does', 'each', 'else', 'hadn', 'hasn', 'have', 'have', 'hers', 'just', 'more', 'most', 'much', 'must', 'need', 'only', 'ours', 'same', 'shan', 'some', 'such', 'than', 'that', 'that', 'them', 'then', 'they', 'this', 'this', 'very', 'wasn', 'were', 'were', 'what', 'when', 'whom', 'will', 'will', 'with', 'your', 'being', 'being', 'could', 'doesn', 'doing', 'doing', 'haven', 'might', 'mustn', 'needn', 'other', 'ought', 'shall', 'their', 'these', 'these', 'those', 'those', 'until', 'weren', 'where', 'which', 'while', 'would', 'yours', 'couldn', 'having', 'having', 'itself', 'mightn', 'myself', 'should', 'should', 'should', 'theirs', 'wouldn', 'because', 'herself', 'himself', 'shouldn', 'similar', 'yourself', 'ourselves', 'themselves', 'yourselves'}


def get_audio_prompt(prompt: str):
    result = send_to_openai_completion(_make_audio_prompt(prompt), 10)
    resultArray = result.strip().replace('"', ' ').replace("'", ' ').replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace(';', ' ').replace('-', ' ').replace('_', ' ').replace(':', ' ').replace(';', ' ').split()


    for i, word in enumerate(resultArray):
        if word.lower() in forbidden_words or len(word) < 3 or len(word) > 8 or i == len(resultArray) - 1 or i > 3:
            continue
        return word.lower()

    return get_audio_prompt(prompt)


if __name__ == '__main__':
    print(get_audio_prompt(
        "He did not do so, however, because he knew that it was useless. Whether he wrote DOWN WITH BIG BROTHER, or whether he refrained from writing it, made no differ- ence. Whether he went on with the diary, or whether he did not go on with it, made no difference. The Thought Police would get him just the same. He had committed—would still have committed, even if he had never set pen to pa- per—the essential crime that contained all others in itself. Thoughtcrime, they called it. Thoughtcrime was not a thing that could be concealed for ever. You might dodge success- fully for a while, even for years, but sooner or later they were bound to get you. It was always at night—the arrests invariably happened at night. The sudden jerk out of sleep, the rough hand shak- ing your shoulder, the lights glaring in your eyes, the ring of hard faces round the bed. In the vast majority of cases there was no trial, no report of the arrest. People simply disap- peared, always during the night. Your name was removed from the registers, every record of everything you had ever done was wiped out, your one-time existence was denied and then forgotten. You were abolished, annihilated: VA- PORIZED was the usual word."))
