from Cimpl import choose_file, load_image, show, Image, copy, create_color,set_color, get_color, create_image, \
                  save_as, save, get_height, get_width

from simple_Cimpl_filters import grayscale

import math

def red_channel(original_image) -> Image:
    """ (None) -> Cimpl.Image

    Removes the contribution from green and blue from
    the value of all pixels contained in an image,
    "original_image".

    >>> red_image = red_channel(load_image(choose_file()))
    >>> show(red_image)

    *Red version of selected image where all pixels have a blue and green
    value of 0 and red remains the same appears*

    Examples:
    color of a pixel before and after calling red_channel
    (0,0,0) --------> (0, 0, 0)
    (23,45,200) --------> (23, 0, 0)
    (255,1,2) --------> (255, 0, 0)

    # Author: Orit Hashim
    # Student number: 101142803
    """
    # These are constant values and should not be changed
    REQUIRED_GREEN_VAL = 0
    REQUIRED_BLUE_VAL = 0

    # This makes a copy of the original image
    new_image = copy(original_image)

    for pixel in original_image:
        # Loop iterates though the coordinates and value of each pixel
        x, y, (r, g, b) = pixel
        # keep only the red value of the pixel
        new_colour = create_color(r, REQUIRED_GREEN_VAL, REQUIRED_BLUE_VAL)
        # The next line changes the color of the new image at
        # coordinate x,y to only the r component
        set_color(new_image, x, y, new_colour)

    return new_image


def green_channel(image: Image) -> Image:
    """ Takes an Image and reads the RGB value of each pixel. It then converts
    the pixel and returns a new image with each pixel containing a green value
    with a value of 0 for red and 0 for blue.

    How to use function:
    >>> image = load_image(choose_file()) # loading the image which is located in the same folder as Cimpl
    >>> show(green_channel(image)) # shows the image in a seperate window

    Code by Marcelo Saldivia-Woo, 101087656
    """
    new_image = image  # This assigns the input image to the variable new_image

    green_filter = copy(new_image)  # Creates a copy of the chosen image to work on

    for x, y, (r, g, b) in green_filter:  # x and y are the coordinates of the image, r,g,b represent red, green, blue

        if r != 0 or b != 0:
            set_color(green_filter, x, y, create_color(0, g, 0))  # applies the new rgb colour to the image
    return green_filter


def blue_channel(image: Image) -> Image:
    """ Evalueates the pixels of an image and changes the pixels' rgb values
    to only show blue color
    image = load_image()
    show(blue_channel(image))

    Coded by Juan Pablo Nenclares
    Review by Marcelo Saldivia-Woo
    """

    new_image = image

    blue_filter = copy(new_image)  # Creates a copy of a specific image

    for x, y, (r, g, b) in blue_filter:

        if r != 0 or g != 0:
            set_color(blue_filter, x, y, create_color(0, 0, b))

    return blue_filter


def combine(red:Image, green:Image, blue:Image) -> Image:
    """Returns a new image that combines the colours of each pixel of 3 images into 1. All images inputed
    must have the same dimensions.

    >>>combine(red_image, green_image, blue_image)
    returns a new image based on the dimensions of the red image, with combined RGB values from
    red_image, green_image, and blue_image

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


black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
lime = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]
cyan = [0, 255, 255]
magenta = [255, 0, 255]
gray = [128, 128, 128]


def two_tone(image: Image, colour1, colour2) -> Image:
    """
    Returns a copy of the chosen image with only 2 colours.

    >>>two_tone(image, cyan, magenta)
    returns the same image solely with those 2 colours.

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

        if ((r + g + b) / 3) >= 128:  # sets the pixel colour to the 2nd colour if the brightness is above 128
            set_color(new_image, x, y, new_colour2)

        if ((r + g + b) / 3) <= 127:  # sets the pixel colour to the 1st colour if the brightness is below 128
            set_color(new_image, x, y, new_colour1)

    return new_image


def three_tone(image: Image, colour1, colour2, colour3) -> Image:
    """
    Returns a copy of the chosen image with only 3 colours.

    >>>three_tone(image, cyan, magenta, gray)
    Returns the same image solely with the colours, cyan, magenta, gray

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


def extreme_contrast(image: Image) -> Image:
    """ Takes an image and maximizes the contrast between the red, green and blue
    components of each pixel. The function returns a copy of the original image with the applied
    changes to the components

    Code by Juan Pablo Nenclares, 10112815
    """

    new_image = copy(image)  # Makes a copy of the original image.
    for x, y, (r, g, b) in image:
        if 0 <= r <= 127:
            r = 0  # Sets the r value to 0 if the r value is in between 0 and 127.
        else:
            r = 255  # Otherwise it sets the r value to 255.
        if 0 <= g <= 127:
            g = 0  # Sets the g value to 0 if the g value is in between 0 and 127.
        else:
            g = 255  # Otherwise it sets the g value to 255.
        if 0 <= b <= 127:
            b = 0  # Sets b values to 0 if b values are i between 0 and 127.
        else:
            b = 255  # Otherwise sets the value to 255.

        color = create_color(r, g, b)
        set_color(new_image, x, y, color)  # Applies the new rgb values to every pixel of the image.

    return new_image  # Returns the copy of the altered image.


def sepia(image: Image) -> Image:
    """
    Takes an image and creates a copy that is converted to grayscale, then the red and blue values are assigned new values that are propagated by different values that are used to convert the colours dark gray, medium gray, and light gray creating a sepia tint.

    How to use the function:
    >>> image = load_image(choose_file())
    >>> image_sepia = sepia(image)
    >>> show(image_sepia)


    Code by Marcelo Saldivia-Woo, 101087656
    """

    new_image = image  # this assigns the input image to the variable new_image

    grayscale_image = grayscale(
        new_image)  # this calls upon the imported grayscale function to iterate over new_image and be assigned to variable grayscale image

    sepia_tinted = grayscale_image  # this assigns the grayscale image to the variable sepia_tinted

    for x, y, (r, g, b) in sepia_tinted:

        if b <= 63 and b > 0:  # this will compare the value of b in RGB values, it must be between the two assigned values
            sepia1 = create_color(r * 1.1, g,
                                  b * 0.9)  # this will create the new colour of the pixel from a dark gray pixel
            set_color(sepia_tinted, x, y,
                      sepia1)  # this will assign the new pixel back to the image that is assigned to variable sepia_tinted
        elif r > 63 and r < 191:
            sepia2 = create_color(r * 1.15, g,
                                  b * 0.85)  # this will create the new colour of the pixel from a medium gray pixel
            set_color(sepia_tinted, x, y, sepia2)
        elif r > 191 and r <= 236:
            sepia3 = create_color(r * 1.08, g,
                                  b * 0.93)  # this will create the new colour of the pixel from a light gray pixel
            set_color(sepia_tinted, x, y, sepia3)

    return sepia_tinted  # this will return the new image that has been iterated over by the above code


def _adjust_component(colour_int: int) -> int:
    """ Returns the midpoints of one of the ranges of
    0-63, 64-127, 128-191, or 192- 255
    depending on which range colour_int falls between"

    Caution: colour_int must be in between 0-255 inclusive

    >>>_adjust_component(0)
    31

    >>>_adjust_component(127)
    95

    >>>_adjust_component(191)
    159

    >>> _adjust_component(255)
    223

    # Author: Orit Hashim
    # Student number: 101142803
    """
    boundary_1 = 63
    boundary_2 = 127
    boundary_3 = 191

    if colour_int <= boundary_1:
        return 31
    elif boundary_1 < colour_int <= boundary_2:
        return 95
    elif boundary_2 < colour_int <= boundary_3:
        return 159
    else:
        return 223


def posterize(original_image) -> Image:
    """(Cimpl.Image) -> Cimpl.Image

    Returns a posterized version copy of a chosen image,original_image.
    Each colour component of a pixel will be replaced with
    31 if it falls in the range of 0-63, 95 if it falls in the range
    of 64-127, 159 if in the range of 128-191
    and 223 if higher than 191.

    Example 1:
    >>> original_image = load_image(choose_file())
    >>> r, g, b = get_color(original_image, 20, 50)
    >>> r, g, b
    0, 127, 230
    >>> new_image = posterize(image)
    >>> r,g,b = get_color(new_image, 20, 50)
    >>> r, g, b
    31, 95, 223

    Example 2:
    Color(1, 234, 191) yields to Color(31, 233, 159)

    # Author: Orit Hashim
    # Student number: 101142803
    """
    # This line makes a copy of the original image
    new_image = copy(original_image)

    for pixel in original_image:
        # This iterates though the coordinates and value of each pixel
        x, y, (r, g, b) = pixel
        new_colour = create_color(_adjust_component(r),
                                  _adjust_component(g), _adjust_component(b))
        set_color(new_image, x, y, new_colour)

    return new_image


def detect_edges(image: Image, threshold:int) -> Image:
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


def detect_edges_better(image: Image, threshold: int) -> Image:
    """ Takes an image and produces a new image that is a sketch variant of it

    How to use function:
    >>> image = load_image(choose_file(), threshold)
    >>> sketch = detect_edges_better(image)
    >>> show(sketch) # shows the image in a seperate window

    Code by Marcelo Saldivia-Woo, 101087656
    """

    new_image = copy(image)
    for y in range(get_height(new_image) - 1):
        for x in range(get_width(new_image) - 1):
            r1, g1, b1 = get_color(new_image, x, y)
            r2, g2, b2 = get_color(new_image, x, y + 1)
            r3, g3, b3 = get_color(new_image, x + 1, y)
            con = abs((r1 + g1 + b1) / 3 - (r2 + g2 + b2) / 3)
            con2 = abs((r1 + g1 + b1 / 3) - (r3 + g3 + b3 / 3))

            if con > threshold:
                set_color(new_image, x, y, create_color(0, 0, 0))
            elif con2 > threshold:
                set_color(new_image, x, y, create_color(0, 0, 0))
            else:
                set_color(new_image, x, y, create_color(255, 255, 255))

    for x in range(get_width(new_image)):
        set_color(new_image, x, get_height(new_image) - 1, create_color(255, 255, 255))
    return new_image


def flip_vertical(original_image) -> Image:
    """ (Cimpl.Image) -> Cimpl.Image

    Returns a copy of a chosen image,original_image,
    that is now filpped across the vertical axes.

    How to use the function:
    >>> image = load_image(choose_file())
    >>> flipped = filp_vertical(image)
    >>> show(filpped)


    Example 1:
    >>> original_image = load_image(choose_file())
    >>> get_width(original_image)
    400
    >>> get_height(original_image)
    200
    >>> r, g, b = get_color(original_image, 20, 50)
    >>> r, g, b
    0, 127, 230
    >>> r, g, b = get_color(original_image, 360, 50)
    >>> r, g, b
    110, 100, 230
    >>> flipped = filp_vertical(original_image)
    >>> r, g, b = get_color(flipped, 20, 50)
    110, 100, 230
    r, g, b = get_color(flipped, 360, 50)
    0, 127, 230

    Example 2:
    In original_image the colour of pixel at cooridinates
    (10,100) is Color(r = 100, g = 400, b = 20)
    and the colour of pixel at cooridinates
    (390,100) is Color(r = 200, g = 300, b = 40)
    After running "flip_vertical(original_image)"
    Coordinates: (10, 100)  ---> Color: Color(r = 200, g = 300, b = 40)
    Coordinates: (390, 100)  ---> Color(r = 100, g = 400, b = 20)

    # Author: Orit Hashim
    # Student number: 101142803
    """
    # This line makes a copy of the original image
    new_image = copy(original_image)
    image_height = get_height(new_image)
    image_width = get_width(new_image)

    for i in range(image_height):

        # It is neccessary only to flip half of the image
        for j in range(math.ceil(image_width / 2)):
            color_original = get_color(original_image, j, i)
            color_flipped = get_color(original_image, (image_width - j) - 1, i)
            # The next two lines switch the color at pixel "x" spaces from
            # the far left with the color at "x" pixels from the far right
            set_color(new_image, j, i, color_flipped)
            set_color(new_image, (image_width - j) - 1, i, color_original)

    return new_image


def flip_horizontal(image: Image) -> Image:
    """Returns the copy of image that has been flipped on its horizontal axis
    >>> image = load_image(choose_file())
    >>> flip_horizontal(image)

    Code by Juan Pablo Nenclares, 10112815
    """

    centre_height = get_height(image) // 2  # Sets a variable for the midpoint between two pixels.
    width = get_width(image)  # Defines the pixels on the width dimension of the image
    height = get_height(image)  # Defines the pixels on the height dimension of the image
    for x in range(width):
        for y in range(centre_height):
            r, g, b = get_color(image, x, y)
            r2, g2, b2 = get_color(image, x, height - y - 1)  # Flips the color of the pixels along the horizontal axis
            set_color(image, x, y, create_color(r2, g2, b2))
            set_color(image, x, height - y - 1, create_color(r, g, b))

    show(image)
    return image

