from truchet import truchet_tile, truchet_image
from image_tools import array_to_image, image_to_array, load_image


def truchet_tile():
    size: int = 64
    image = array_to_image(truchet_tile(size, 0.7, 0, 'quadratic'))
    image.save("test.png")


def truchet_image():
    # TODO: Command line arguments!!!
    name = "test.png"
    file = "input/" + name
    out = "output/" + name
    arr = image_to_array(load_image(file))
    new_img = array_to_image(truchet_image(arr, 10, [[2,3],[0,1]], 256))
    new_img.save(out)


truchet_image()
#truchet_tile()
