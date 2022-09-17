import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def _make_prompt(prompt: str):
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
           "Q: Write a comma separated text prompt for a AI art generation software that would best describe the scene from the following sentence: \"{prompt}\"." \
           "A:".format(prompt=prompt)


def get_image_prompt(prompt: str):
    response = openai.Completion.create(
        engine="davinci",
        prompt=_make_prompt(prompt),
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n", " Human:", " AI:"]
    )
    return response.choices[0].text
