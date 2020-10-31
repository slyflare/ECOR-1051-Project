from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_color, create_image, \
    save_as, save

# Orit Hashim
def red_channel():
    """ (None) -> Cimpl.Image

    removes the contribution from green and blue from the value of all pixels contained in an image

      >>> red_image = red_channel()
      >>> show(red_image)
      *Red version of selected image where all pixels have a blue and green value of 0 and red remains the same appears*

    """
    RequiredGreenVal = 0
    RequiredBlueVal = 0

    original_image = load_image(choose_file())
    new_image = copy(original_image)  # makes a copy of the original image
    for pixel in original_image:
        x, y, (r, g, b) = pixel  # interates though the coordinates and value of each pixel
        new_colour = create_color(r, RequiredGreenVal, RequiredBlueVal)  # keep only the red value of the pixel
        set_color(new_image, x, y, new_colour)  # changes the color of the new image at coordinate x,y to r
    save_as(new_image,'red.png')
    show(load_image('red.png'))


def check_equal(description: str, outcome,
                expected) -> int:  # (prof's method) -- using given function just in case we have to
    """
    Returns 1 if either the type of expected and outcome do not match or if expected and outcome are not equal(==)
    to each other. Parameter "description" should provide information that will help
    interpret the test results; e.g., the call expression that yields
    outcome.


    >>>check_equal("Checking pixel @(0, 0)", 1, 1)


    >>> check_equal("Checking pixel @(0, 0)", 1, "1")
    Checking pixel @(0, 0) FAILED: expected (1) has type int, " \
              "but outcome ("1") has type str

     >>> check_equal("Checking pixel @(0, 0)", 1, 0)
     Checking pixel @(0, 0) FAILED: expected 0, got 1"
    """

    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:  # prints fail statement if the types of the expected and outcome are not the same
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '),
                     outcome, str(outcome_type).strip('<class> ')))
        return 1
    elif outcome != expected:  # prints fail statements if the expected value does not equal the outcome value
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
        return 1
    else:
        return 0


def red_test_filters(
        red_image):  # will call on the professor's method. The purpose of this method is to only call on check_equal
    # if a test is failed
    """
    Cimpl.Image -> None

    Tests an image, red_image,  to enure that the values of green and blue of each pixel is zero.

    >>> red_test_filters(red_channel())
    all pixels PASSED

    if one blue pixel at coordinate (0,0) where (57,0,0) is expected:
    >>>red_test_filters(image)
    red_channel() at coordinates (0,0) FAILED: expected (57, 0, 0), got (0,0,255)

    """

    list_of_gb_values = []
    counter = 0
    RequiredGreenVal = 0
    RequiredBlueVal = 0

    for pixel in red_image:
        x, y, (r, g, b) = pixel
        list_of_gb_values += [(g, b)]  # adds the green and blue values of every pixel to a list in the form of tuples

    for i in list_of_gb_values:
        counter += check_equal("red_channel() at coordinates {}".format((x, y)), (r, g, b),
                               (r, RequiredGreenVal, RequiredBlueVal))

    if counter == 0:  # prints only if there are no failures
        print("all pixels PASSED")


# Marcelo Saldivia-Woo:
def green_channel():
    """ Takes an image and creates an image applied with a green filter

    """

    photo = "p2-original.jpg"

    original_image = load_image(photo)  # loading the image which is located in the same folder as Cimpl

    new_image = copy(original_image)  # creates a copy of the chosen image to work on

    for pixel in new_image:
        x, y, (r, g, b) = pixel  # x and y are the coordinates of the image, r,g,b represent red, green, blue
        new_color = create_color(0, g, 0)  # red and blue values are 0, so only green values will be present
        set_color(new_image, x, y, new_color)  # applies the new rgb colour to the image
    save_as(new_image, "green.png")  # saves the green version of the image
    show(load_image("green.png"))  # opens the green version of the image


def green_test():
    """Tests green_channel function"""
    image = load_image("p2-green.png")  # loads the image to be tested
    for pixel in image:  # variable pixel is assigned to variable image
        x, y, (r, g, b) = pixel  # defines the variable pixel
        if (r, g, b) != (0, g, 0):  # Checks if the values of r,b,g are not equal to (0,g,0)
            print("Test Failed at pixel", x, y, (r, g, b))
        else:
            return "All other pixels are now green"


# Juan Pablo Nenclares:
def blue_channel():
    """Returns a copy of the original image, removing the r and g values from
    the pixels"""

    image = load_image('blue_image.jpg')
    new_image = copy(image)
    for x, y, (r, g, b) in new_image:
        blue = create_color(0, 0, b)
        set_color(new_image, x, y, blue)
    save_as(new_image, 'blue.png')
    show(load_image('blue.png'))


def test_blue_channel():
    """Returns 'Test Passed' if new image only has the blue element of rbg in
    every pixel
    """
    new_image = load_image('blue.png')
    count = 0
    for i in new_image:
        x, y, (r, g, b) = i

        if r != 0 or g != 0:
            print("Test Failed at Pixel:", i)
            count += 1
    if count == 0:
        print("Test Passed")

# Vimal Gunasegaran:
def combine():
    """Returns a new image that combines the colours of each pixel of 3 images into 1.
    # Coded by Vimal Gunasegaran
    """
    r_image = load_image('red.png')
    g_image = load_image('green.png')
    b_image = load_image('blue.png')

    new_image = create_image(640, 480)

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

    save_as(new_image, 'combined_image.png')
    show(load_image('combined_image.png'))

def combine_test():
    """Tests combine()"""
    combined = load_image('combined_image.png')
    original = load_image('p2-original.jpg')

    rgb_combined = []
    rgb_original = []

    for x, y, (r, g, b) in combined:
        rgb_combined.append((r, g, b))
    for x, y, (r, g, b) in original:
        rgb_original.append((r, g, b))
    for i in range(len(rgb_original)):
        if rgb_original[i] != rgb_combined[i]:
            print('test failed at pixel ' + str(i+1), rgb_original[i], rgb_combined[i])
    return 'All other pixels passed'


red_channel()
blue_channel()
green_channel()
combine()