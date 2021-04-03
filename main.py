from truchet import truchet_tile, truchet_image
from image_tools import array_to_image, image_to_array, load_image


def test_truchet_tile():
    size: int = 64
    image = array_to_image(truchet_tile(size, 0, 3))
    image.save("test.png")


def test_truchet_image():
    file = "input/jesus.jpg"
    out = "output/jesus.jpg"
    arr = image_to_array(load_image(file))
    new_img = array_to_image(truchet_image(arr, 20, [[2,3],[1,0]]))
    new_img.save(out)


test_truchet_image()
