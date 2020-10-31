# Code by by Vimal Gunasegaran
# 101155249

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_color, create_image, \
    save_as, save, get_height, get_width


def detect_edges(image: Image, threshold:int):
    """Takes in an image and a int value for contrast and returns a new image with solely the outlines. The function
    compare the contrast of 2 vertical pixels and change the colour to either black or white if the contrast
    is larger then the set threshold. The new returned image will look very much like a pencil sketch.

    #Coded by Vimal Gunasegaran, 101155249
    """
    new_image = copy(image)
    for y in range(get_height(new_image)-1):  # Goes through each column except the very last one
        for x in range(get_width(new_image)):  # Goes through each x value in that column
            r1, g1, b1 = get_color(new_image, x, y)
            r2, g2, b2 = get_color(new_image, x, y + 1)
            con = abs((r1+g1+b1)/3 - (r2+g2+b2)/3)  # compares the colours of the 2 pixels and calculates contrast

            if con > threshold:  # if contrast is above threshold, then the pixel colour is black, else its white
                set_color(new_image, x, y, create_color(0, 0, 0))
            else:
                set_color(new_image, x, y, create_color(255, 255, 255))

    for x in range(get_width(new_image)):  # sets the every last column white.
        set_color(new_image, x, get_height(new_image)-1, create_color(255, 255, 255))
    return new_image


show(detect_edges(load_image('miss_sullivan.jpg'), 12))
