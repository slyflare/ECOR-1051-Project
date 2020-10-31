# Code by by Vimal Gunasegaran
# 101155249

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_color, create_image, \
    save_as, save, get_height, get_width

from T25_P2_filter_combine import combine


def combine_test():
    """Tests the combine function
    >>>combine_test()
    Pixel at (0,0) passed.
    Pixel at (0,1) passed.
    Pixel at (0,2) passed.

    # Coded by Vimal Gunasegaran, 101155249
    """

    red = create_image(1, 3, create_color(255, 0, 0))
    green = create_image(1, 3, create_color(0, 255, 0))
    blue = create_image(1, 3, create_color(0, 0, 255))

    expected = create_image(1, 3, create_color(255, 255, 255))

    result = combine(red, green, blue)

    for x, y, (r, g, b) in result:
        if (r, g, b) == tuple(get_color(expected, x, y)):
            print("Pixel at (" + str(x) + "," + str(y) + ") passed.")
        else:
            print("Pixel at (" + str(x) + "," + str(y) + ") failed. Expected " + str((r, g, b)) + " got "
                  + str(get_color(expected, x, y)))
