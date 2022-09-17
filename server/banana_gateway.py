import base64
import json
import time
import banana_dev as banana
from joblib import Parallel, delayed
import os
import random

api_key = os.getenv('BANANA_API_KEY')
model_key = os.getenv('BANANA_MODEL_KEY')

id = time.time()

# if images folder doesn't exist, create it
if not os.path.exists("./images"):
    os.makedirs("./images")

# mkdir with name 'start'
# in python
os.mkdir(f'./images/{id}')


def process(job):
    start = time.time()
    print(f'Starting prompt: "{job}"')

    # make seed a completely random number independent of time
    seed = random.randint(0, 1000000)

    # or set a custom seed, uncomment below
    # seed = 42

    model_inputs = {
        # a json specific to your model. For example:
        "prompt": job,
        "height": 512,
        "width": 1024,
        'seed': seed,
        'num_reference_steps': 150,
        'columns': 1,
        'rows': 1,
        'guidance_scale': 7.0,
        'upscale': False
    }

    out = banana.run(api_key, model_key, model_inputs)

    # save out as a base64 image to disk
    # save obj (type String) as an image to disk
    # name the images with the index of the image in the queue
    with open(f'./images/{id}/{i}.png', "wb") as fh:
        fh.write(base64.b64decode(out['modelOutputs'][0]["image_base64"]))

    # End the timer
    end = time.time()
    print("Time elapsed: ", end - start)


def create_image(queue):
    Parallel(n_jobs=1)(delayed(process)(job) for job in queue)

    return
