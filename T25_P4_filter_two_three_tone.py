# Code by by Vimal Gunasegaran
# 101155249

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_color, create_image, \
    save_as, save

black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
lime = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]
cyan = [0, 255, 255]
magenta = [255, 0, 255]
gray = [128, 128, 128]


def two_tone(image: Image, colour1, colour2):
    """
    Returns a copy of the chosen image with only 2 colours.

    Colour inputs:
    black
    white
    red
    lime
    blue
    yellow
    cyan
    magenta
    gray

    # Coded by Vimal Gunasegaran
    """
    new_image = copy(image)

    for x, y, (r, g, b) in new_image:
        new_colour1 = create_color(colour1[0], colour1[1], colour1[2])
        new_colour2 = create_color(colour2[0], colour2[1], colour2[2])

        if ((r + g + b) / 3) >= 128:  # sets the pixel colour to the 2nd colour if the brightness is above 128
            set_color(new_image, x, y, new_colour2)

        if ((r + g + b) / 3) <= 127:  # sets the pixel colour to the 1st colour if the brightness is below 128
            set_color(new_image, x, y, new_colour1)

    return new_image


def three_tone(image: Image, colour1, colour2, colour3):
    """
        Returns a copy of the chosen image with only 3 colours.

        Colour inputs:
        black
        white
        red
        lime
        blue
        yellow
        cyan
        magenta
        gray

        # Coded by Vimal Gunasegaran, 101155249
        """
    new_image = copy(image)

    for x, y, (r, g, b) in new_image:
        new_colour1 = create_color(colour1[0], colour1[1], colour1[2])
        new_colour2 = create_color(colour2[0], colour2[1], colour2[2])
        new_colour3 = create_color(colour3[0], colour3[1], colour3[2])

        if ((r + g + b) / 3) <= 84:  # sets the pixel colour to the 1st colour if the brightness is below 84
            set_color(new_image, x, y, new_colour1)

        if 85 <= ((r + g + b) / 3) <= 170:  # sets the pixel colour to the 2nd colour if the brightness > 85 and < 170
            set_color(new_image, x, y, new_colour2)

        if ((r + g + b) / 3) >= 171:  # sets the pixel colour to the 3rd colour if the brightness is above 170
            set_color(new_image, x, y, new_colour3)
    return new_image


show(two_tone(load_image('riveter.jpg'), cyan, lime))
show(three_tone(load_image('riveter.jpg'), magenta, white, cyan))
