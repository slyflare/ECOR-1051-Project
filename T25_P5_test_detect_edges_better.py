# Code by by Vimal Gunasegaran
# 101155249

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_color, create_image, \
    save_as, save, get_height, get_width

from T25_P5_filter_detect_edges_better import detect_edges_better

def detect_edges_better_test():
    """Tests detect_edges_better()
    >>>detect_edges_better_test()

    #Coded by Vimal Gunasegaran, 101155249
    """
    original = create_image(7, 3, create_color(85, 85, 85))  # Creates an image that is put through detect_edges_better
    set_color(original, 1, 0, create_color(255, 255, 255))
    set_color(original, 2, 1, create_color(255, 255, 255))
    set_color(original, 2, 2, create_color(255, 255, 255))
    set_color(original, 3, 0, create_color(255, 255, 255))
    set_color(original, 3, 1, create_color(255, 255, 255))
    set_color(original, 3, 2, create_color(255, 255, 255))
    set_color(original, 4, 1, create_color(255, 255, 255))
    set_color(original, 6, 0, create_color(255, 255, 255))
    set_color(original, 6, 1, create_color(255, 255, 255))

    expected = create_image(7, 3, create_color(255, 255, 255))  # Creates an image with the expected result
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 1, 1, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 0))
    set_color(expected, 4, 0, create_color(0, 0, 0))
    set_color(expected, 4, 1, create_color(0, 0, 0))
    set_color(expected, 5, 0, create_color(0, 0, 0))
    set_color(expected, 5, 1, create_color(0, 0, 0))

    test = detect_edges_better(original, 100)  # Loops through each pixel and compares the result with the expected.
    for x, y, (r, g, b) in test:
        if (r, g, b) == tuple(get_color(expected, x, y)):
            print("Pixel at (" + str(x) + "," + str(y) + ") passed.")
        else:
            print("Pixel at (" + str(x) + "," + str(y) + ") failed. Expected " + str((r, g, b)) + " got "
                  + str(get_color(expected, x, y)))


detect_edges_better_test()
