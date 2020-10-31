

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color


def grayscale_from_blue(image: Image, a:int) -> Image:
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        new_colour = create_color(r % a, g % a, b % a)
        set_color(new_image, x, y, new_colour)
    return new_image


show(grayscale_from_blue(load_image('miss_sullivan.jpg'), 200))
