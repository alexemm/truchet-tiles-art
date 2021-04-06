from truchet import truchet_tile, truchet_image
from image_tools import array_to_image, image_to_array, load_image


def test_truchet_tile():
    size: int = 64
    image = array_to_image(truchet_tile(size, 0.7, 0, 'quadratic'))
    image.save("test.png")


def test_truchet_image():
    name = "jesus.jpg"
    file = "input/" + name
    out = "output/" + name
    arr = image_to_array(load_image(file))
    new_img = array_to_image(truchet_image(arr, 10, [[2,3],[0,1]], 64))
    new_img.save(out)


#test_truchet_image()
test_truchet_tile()
