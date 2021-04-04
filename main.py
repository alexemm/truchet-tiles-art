from truchet import truchet_tile, truchet_image
from image_tools import array_to_image, image_to_array, load_image


def test_truchet_tile():
    size: int = 64
    image = array_to_image(truchet_tile(size, 0.60, 0))
    image.save("test.png")


def test_truchet_image():
    name = "rick.png"
    file = "input/" + name
    out = "output/" + name
    arr = image_to_array(load_image(file))
    new_img = array_to_image(truchet_image(arr, 3, [[2,3],[0,1]], 32))
    new_img.save(out)


test_truchet_image()
#test_truchet_tile()
