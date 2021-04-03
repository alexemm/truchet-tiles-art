from truchet import truchet_tile
from image_tools import array_to_image, image_to_array


def test():
    size: int = 64
    image = array_to_image(truchet_tile(64, 1, 3))
    image.save("test.png")

test()
