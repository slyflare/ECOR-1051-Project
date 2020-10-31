# Code by by Vimal Gunasegaran
# 101155249

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_color, create_image, \
    save_as, save, get_height, get_width


def combine(red:Image, green:Image, blue:Image):
    """Returns a new image that combines the colours of each pixel of 3 images into 1.

    # Coded by Vimal Gunasegaran, 101155249
    """
    r_image = copy(red)
    g_image = copy(green)
    b_image = copy(blue)

    new_image = create_image(get_width(red), get_height(red))

    r_colour = []
    g_colour = []
    b_colour = []

    for x, y, (r, g, b) in r_image:
        r_colour.append(r)

    for x, y, (r, g, b) in g_image:
        g_colour.append(g)

    for x, y, (r, g, b) in b_image:
        b_colour.append(b)

    i = 0
    for x, y, (r, g, b) in new_image:
        new_colour = create_color(r_colour[i], g_colour[i], b_colour[i])
        set_color(new_image, x, y, new_colour)

        i += 1

    return new_image



