# Code by by Vimal Gunasegaran
# 101155249

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_color, create_image, \
    save_as, save

from T25_P4_filter_sepia import sepia


def test_sepia():
    '''Tests sepia()
    >>>test_sepia()
    Pixel at (0,0) passed.
    Pixel at (1,0) passed.
    Pixel at (2,0) passed.
    Pixel at (3,0) passed.

    #Coded by Vimal Gunasegaran, 101155249
    '''

    original = create_image(4, 1)  # Creates a new image that will be put through the sepia function
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(62, 64, 60))
    set_color(original, 2, 0, create_color(64, 255, 64))
    set_color(original, 3, 0, create_color(231, 229, 230))

    expected = create_image(4, 1)  # Creates a new image with the expected result of sepia(original)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(68, 62, 55))
    set_color(expected, 2, 0, create_color(146, 127, 107))
    set_color(expected, 3, 0, create_color(248, 230, 213))

    test = sepia(original)
    for x, y, (r, g, b) in test:  # Runs through each pixel and compares the result with the expected.
        if (r, g, b) == tuple(get_color(expected, x, y)):
            print("Pixel at (" + str(x) + "," + str(y) + ") passed.")
        else:
            print("Pixel at (" + str(x) + "," + str(y) + ") failed. Expected " + str((r, g, b)) + " got "
                  + str(get_color(expected, x, y)))


test_sepia()
