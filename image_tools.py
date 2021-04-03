
from typing import List, Tuple

import numpy as np
from PIL import Image, ImageDraw
from os import listdir, makedirs

def load_image(file: str):
    im = Image.open(file).convert('L')
    return im


def image_to_array(img):
    return np.asarray(img)


def array_to_image(arr):
    return Image.fromarray(np.uint8(arr))


