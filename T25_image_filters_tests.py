from Cimpl import choose_file, load_image, show, Image, copy, create_color,set_color, get_color, create_image, \
                  save_as, save, get_height, get_width

from T25_image_filters import red_channel, green_channel, blue_channel, combine, two_tone, three_tone, \
    sepia, extreme_contrast, posterize, detect_edges, detect_edges_better, flip_vertical, flip_horizontal


def check_equal(description: str, outcome, expected) -> int:
    # (prof's method) with small edits
    """ Returns 1 if either the type of expected and outcome do not
    match or if expected and outcome are not equal(==)
    to each other. Parameter "description" should provide information
    that will help interpret the test results;
    e.g., the call expression that yields outcome.


    >>>check_equal("Checking pixel @(0, 0)", 1, 1)


    >>> check_equal("Checking pixel @(0, 0)", 1, "1")
    Checking pixel @(0, 0) FAILED: expected (1) has type int, \
    but outcome ("1") has type str

     >>> check_equal("Checking pixel @(0, 0)", 1, 0)
     Checking pixel @(0, 0) FAILED: expected 0, got 1

    """

    outcome_type = type(outcome)
    expected_type = type(expected)
    # prints fail statement if the types of the expected
    # and outcome are not the same

    if outcome_type != expected_type:
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '),
                     outcome, str(outcome_type).strip('<class> ')))
        return 1
    # prints fail statements if the expected value does not equal
    # the outcome value
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
        return 1
    else:
        return 0


def test_red() -> None:
    '''A test function for red_channel.

    If red_channel works

    >>> test_red()
    all pixels PASSED

    If red_channel fails at pixel with coordinates (1,0)
    where the value is (red=0, green=127, blue=1)
    and should be (red=0, green=0, blue=0)

    >>> test_red()
    Checking pixel  at coordinates (1, 0) FAILED:
    expected Color(red=0, green=127, blue=1), got
    Color(red=0, green=0, blue=0)

    # Author: Orit Hashim
    # Student number: 101142803
    '''

    # This test function checks if red_channel correctly transforms:
    # (0, 0, 0) to (0, 0, 0)
    # (0, 127, 1) to (0, 0, 0)
    # (128, 128, 128) to (128, 0, 0)
    # (125, 73, 224) to (125, 0, 0)
    # (18, 6, 2) to (18, 0,0)

    counter = 0
    # This creates the original photo
    original = create_image(5, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 127, 1))
    set_color(original, 2, 0, create_color(128, 128, 128))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 4, 0, create_color(18, 6, 2))

    # This creates the expected photo after original photo is run
    # though red_channel
    expected = create_image(5, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(128, 0, 0))
    set_color(expected, 3, 0, create_color(125, 0, 0))
    set_color(expected, 4, 0, create_color(18, 0, 0))

    red_image = red_channel(original)

    # col is the Color object for the pixel @ (x,y)
    for x, y, col in red_image:
        description_check_equals = "Checking pixel  at coordinates {}".format((x, y))
        counter += check_equal(description_check_equals,
                               col, get_color(expected, x, y))
    if counter == 0:
        # This prints only if there are no discrepancies between the
        # expected image and the image created by red_channel
        print("all pixels PASSED")


def test_green_channel() -> None:
    """ This function is a test function for the green_channel filter
     If detect_edges function works each pixel will show for each x,y coordinate

    >>>test_green_channel
    >>>pixel at (x,y) PASSED

    If green_channel does not work at pixel coordinates(1,0) where the original value in RGB is (128,128,128) and the expected is (0,128,0)

    >>>test_green_channel
    >>>Checking pixel @(1, 0) FAILED: expected Color(red=0, green=128, blue=0), got Color(red=128, green=128, blue=128)


    Code by Marcelo Saldivia-Woo, 101087656
    """

    # Code is taken from Professor Cheryl Schramm, edited by Marcelo Saldivia-Woo
    problem = 0
    # This test function checks if the green_channel filter will iterate properly over the given image
    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(128, 128, 128))
    set_color(original, 2, 0, create_color(60, 120, 60))
    set_color(original, 3, 0, create_color(255, 255, 255))
    set_color(original, 4, 0, create_color(140, 10, 140))
    set_color(original, 5, 0, create_color(0, 150, 150))

    # Create an image that's identical to the one a correct implementation of
    # green_channel should produce when it is passed original.

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 128, 0))
    set_color(expected, 2, 0, create_color(0, 120, 0))
    set_color(expected, 3, 0, create_color(0, 255, 0))
    set_color(expected, 4, 0, create_color(0, 10, 0))
    set_color(expected, 5, 0, create_color(0, 150, 0))

    green_channel_trial = green_channel(original)
    check = 0
    problem = 0
    for x, y, col in green_channel_trial:  # col is the Color object for the pixel @ (x,y).
        check += check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))
        if check != 0:  # this will compare the expected values with the green_channel function's output of the original values
            problem += 1  # this indicates that there are inconsistent values between expected and the green_channel function
        print("pixel at {}".format((x, y)), "PASSED")


def test_blue_channel() -> None:
    """ Test function for blue filter, where the pixels are evaluated after the filter is applied,

    It compares if the function correctly changes the rgb values to only show blue color.
    >>>pixel at (x,y) PASSED

    If green_channel does not work at pixel coordinates(1,0) where the original value in RGB is (0,127,1) and the expected is (0,0,1)

    Checking pixel  at coordinates (1, 0) FAILED: expected Color(red=0, green=0, blue=1), got Color(red=0, green=127, blue=1)

    Code by Juan Pablo Nenclares, 10112815
    """
    counter = 0
    original = create_image(5, 1)  # Shows the rgb values for the origial photo
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 127, 1))
    set_color(original, 2, 0, create_color(128, 128, 128))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 4, 0, create_color(255, 255, 255))

    expected = create_image(5,
                            1)  # Shows what the altered rgb values of specific pixels should be  after the filter is applied.
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 1))
    set_color(expected, 2, 0, create_color(0, 0, 128))
    set_color(expected, 3, 0, create_color(0, 0, 224))
    set_color(expected, 4, 0, create_color(0, 0, 255))

    blue_image = blue_channel(original)
    for x, y, col in blue_image:
        counter += check_equal("Checking pixel  at coordinates {}".format((x, y)),
                               col, get_color(expected, x, y))
    if counter == 0:
        print("all pixels pass")


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


def test_two_tone() -> None:
    """ This function is a test function for the two_tone filter
     If two_tone function works each pixel will show for each x, y coordinate

    >>> test_two_tone
    >>> pixel at (x, y) PASSED

    If two_tone does not work at pixel coordinates(3, 0) where the original value in RGB is (128, 128, 128) and the expected is (255, 0, 255)

    >>> test_two_tone()
    >>> Checking pixel @(3, 0) FAILED: expected Color(red=255, green=0, blue=255), got Color(red=0, green=255, blue=255)

    Code by Marcelo Saldivia-Woo, 101087656
    """

    # These are different RGB orientations that represent the given colours
    black = [0, 0, 0]
    white = [255, 255, 255]
    red = [255, 0, 0]
    lime = [0, 255, 0]
    blue = [0, 0, 255]
    yellow = [255, 255, 0]
    cyan = [0, 255, 255]
    magenta = [255, 0, 255]
    gray = [128, 128, 128]

    # The chosen colors for this test are cyan and magenta
    # Code is taken from Professor Cheryl Schramm, edited by Marcelo Saldivia-Woo
    problem = 0
    # This test function checks if the two_tone filter will iterate properly over the given image
    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(60, 120, 60))
    set_color(original, 2, 0, create_color(140, 128, 180))
    set_color(original, 3, 0, create_color(128, 128, 128))
    set_color(original, 4, 0, create_color(127, 127, 127))
    set_color(original, 5, 0, create_color(255, 255, 255))

    # Create an image that's identical to the one a correct implementation of
    # two_tone should produce when it is passed original.

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(0, 255, 255))
    set_color(expected, 1, 0, create_color(0, 255, 255))
    set_color(expected, 2, 0, create_color(255, 0, 255))
    set_color(expected, 3, 0, create_color(255, 0, 255))
    set_color(expected, 4, 0, create_color(0, 255, 255))
    set_color(expected, 5, 0, create_color(255, 0, 255))

    two_tones = two_tone(original, cyan, magenta)
    problem = 0
    for x, y, col in two_tones:  # col is the Color object for the pixel @ (x,y).
        check = check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))
        if check != 0:  # this will compare the expected values with the two_tone function's output of the original values
            problem += 1  # this indicates that there are inconsistent values between expected and the two_tone function
        else:  # this will print only if there are no problems found through the check_equal function
            print("pixel at {}".format((x, y)), "PASSED")


def test_three_tone() -> None:
    """ This function is a test function for the two_tone filter
    If three_tone function works

    >>> test_three_tone
    >>> pixel at (1, 0) PASSED

    If three_tone does not work at pixel coordinates(3,0) where the original value in RGB is (128, 128, 128) and the expected is (255, 0, 0)

    test_three_tone()
    >>> Checking pixel @(3, 0) FAILED: expected Color(red=255, green=0, blue=0), got Color(red=255, green=255, blue=255)

    Code by Marcelo Saldivia-Woo, 101087656
    """

    # These are different RGB orientations that represent the given colours
    black = [0, 0, 0]
    white = [255, 255, 255]
    red = [255, 0, 0]
    lime = [0, 255, 0]
    blue = [0, 0, 255]
    yellow = [255, 255, 0]
    cyan = [0, 255, 255]
    magenta = [255, 0, 255]
    gray = [128, 128, 128]
    # The chosen colors for this test are white, red, and magenta

    # Code  is taken from Professor Cheryl Schramm, edited by Marcelo Saldivia-Woo
    problem = 0
    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(60, 120, 60))
    set_color(original, 2, 0, create_color(140, 128, 180))
    set_color(original, 3, 0, create_color(128, 128, 128))
    set_color(original, 4, 0, create_color(240, 200, 100))
    set_color(original, 5, 0, create_color(255, 255, 255))

    # Create an image that's identical to the one a correct implementation of
    expected = create_image(6, 1)  # The values that three_tone should produce when it is passed original.
    set_color(expected, 0, 0, create_color(255, 255, 255))
    set_color(expected, 1, 0, create_color(255, 255, 255))
    set_color(expected, 2, 0, create_color(255, 0, 0))
    set_color(expected, 3, 0, create_color(255, 0, 0))
    set_color(expected, 4, 0, create_color(255, 0, 255))
    set_color(expected, 5, 0, create_color(255, 0, 255))

    problem = 0
    three_tones = three_tone(original, white, red, magenta)
    for x, y, col in three_tones:  # col is the Color object for the pixel @ (x,y).
        check = check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))
        if check != 0:  # this will compare the expected values with the two_tone function's output of the original values
            problem += 1  # this indicates that there are inconsistent values between expected and the three_tone function
        else:
            # this will print only if there are no problems found through the check_equal function
            print("pixel at {}".format((x, y)), "PASSED")


def test_extreme_contrast() -> None:
    '''A test function for extreme contrast.

    If extreme_contrast works

    >>> test_extreme_contrast()
    all pixels PASSED

    If extreme_contrast fails at pixel with coordinates
    (1,0) where the value is (red=0, green=127, blue=1)
    and should be (red=0, green=0, blue=0)

    >>> test_extreme_contrast()
    Checking pixel  at coordinates (1, 0) FAILED:
    expected Color(red=0, green=127, blue=1),
    got Color(red=0, green=0, blue=0)

    # Author: Orit Hashim
    # Student number: 101142803
    '''

    # This test function checks if extreme_contrast
    # correctly transforms:
    # (0, 0, 0) to (0, 0, 0)  # The darkest shade
    # (0, 127, 1) to (0, 0, 0)  # The values at boundary points
    # (128, 128, 128) to (255, 255, 255)  # The values at boundary points
    # (125, 73, 224) to (0, 0, 255)   # the values in both ranges
    # (255, 255, 255) to (255, 255, 255)  # the brightest shade

    counter = 0
    # this line creates the original photo
    original = create_image(5, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 127, 1))
    set_color(original, 2, 0, create_color(128, 128, 128))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 4, 0, create_color(255, 255, 255))

    # Will create expected photo after original photo is run though
    # extreme_contrast
    expected = create_image(5, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(255, 255, 255))
    set_color(expected, 3, 0, create_color(0, 0, 255))
    set_color(expected, 4, 0, create_color(255, 255, 255))

    contrasted_image = extreme_contrast(original)
    # col is the Color object for the pixel @ (x,y)
    for x, y, col in contrasted_image:
        description_check_equals = "Checking pixel  at coordinates {}".format((x, y))
        counter += check_equal(description_check_equals,
                               col, get_color(expected, x, y))
        # This prints only if there are no discrepancies between the
    # expected image and the image created by extreme_constrast*/
    if counter == 0:
        print("all pixels PASSED")


def test_sepia() -> None:
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


def test_posterize() -> None:
    """ Test fuction for posterizing filter. Determines if the filter correctly replaces
    a pixel's colour components for 31  if it falls within the range 0-63, 95 if it falls within
    64-127, 159 if it falls within 128-191 and 223 if the value if higher than 191.

    >>> test_posterize() # test function passes if the function correctly applies the changes to the rgb values.
    all pixels pass

    >>> test_posterize() # If the test function does not apply the values correctly it will display the following message.
    Checking pixel  at coordinates (1, 0) FAILED: expected Color(red=0, green=127, blue=1), got Color(red=31, green=95, blue=159)

    Code by Juan Pablo Nenclares, 10112815
    """
    counter = 0
    original = create_image(5, 1)  # Shows the rgb values for the origial photo
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 127, 1))
    set_color(original, 2, 0, create_color(128, 128, 128))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 4, 0, create_color(255, 255, 255))

    expected = create_image(5,
                            1)  # Shows what the altered rgb values of specific pixels should be  after the filter is applied.
    set_color(expected, 0, 0, create_color(31, 31, 31))
    set_color(expected, 1, 0, create_color(31, 95, 31))
    set_color(expected, 2, 0, create_color(159, 159, 159))
    set_color(expected, 3, 0, create_color(95, 95, 223))
    set_color(expected, 4, 0, create_color(223, 223, 223))

    posterized_image = posterize(original)
    for x, y, col in posterized_image:
        counter += check_equal("checking pixel  at coordinates {}".format((x, y)),
                               col, get_color(expected, x, y))
    if counter == 0:
        print("all pixels pass")


def test_detect_edges() -> None:
    """ This function is a test function for the detect_edges filter
     If detect_edges function works each pixel will show for each x,y coordinate

    >>> test_detect_edges()
    >>> pixel at (x, y) PASSED

    If detect_edges does not work at pixel coordinates(2, 1) where the original value in RGB is (0, 150, 150) and the expected is (255, 255, 255)

    >>> test_detect_edges()
    >>> Checking pixel @(2, 1) FAILED: expected Color(red= 255, green= 255, blue= 255), got Color(red= 0, green= 0, blue= 0)

    Code by Marcelo Saldivia-Woo, 101087656
    """

    # Code is taken from Professor Cheryl Schramm, edited by Marcelo Saldivia-Woo
    problem = 0
    # This test function checks if the detect_edges filter will iterate properly over the given image
    original = create_image(3, 2)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 0, 1, create_color(128, 128, 128))
    set_color(original, 1, 0, create_color(60, 120, 60))
    set_color(original, 1, 1, create_color(255, 255, 255))
    set_color(original, 2, 0, create_color(140, 0, 140))
    set_color(original, 2, 1, create_color(0, 150, 150))

    # Create an image that's identical to the one a correct implementation of
    # detect_edges should produce when it is passed original.

    expected = create_image(3, 2)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 0, 1, create_color(255, 255, 255))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 1, 1, create_color(255, 255, 255))
    set_color(expected, 2, 0, create_color(255, 255, 255))
    set_color(expected, 2, 1, create_color(255, 255, 255))

    detect_edges_trial = detect_edges(original, 12)
    check = 0
    problem = 0
    for x, y, col in detect_edges_trial:  # col is the Color object for the pixel @ (x,y).
        check += check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))
        if check != 0:
            # this will compare the expected values with the detect_edges function's output of the original values
            problem += 1  # this indicates that there are inconsistent values between expected and the detect_edges function
        print("pixel at {}".format((x, y)), "PASSED")


def detect_edges_better_test() -> None:
    """Tests detect_edges_better()
    >>>detect_edges_better_test()
    Pixel at (0,0) passed.
    Pixel at (0,1) passed.
    Pixel at (0,2) passed.

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


def test_flip_vertical() -> None:
    """Test function for the filter flip_vertical. Checks if the filter correctly fliped the colors of the pixels along a vertical axis

    if test_flip_vertical works each pixel will show for each x,y coordinate

    >>>Checking pixel @(x, y) PASSED

    If flip_vertical does not work at pixel coordinates(4,2) where the original value in RGB is (1,15,1) and the expected is (1,11,5)



    >>>Checking pixel @(4, 2) FAILED: expected Color(red=1, green=11, blue=5), got Color(red=1, green=15, blue=1)

    Code by Juan Pablo Nenclares, 10112815
    """

    original = create_image(5, 3)  # Creates an original image
    set_color(original, 0, 0, create_color(1, 1, 15))
    set_color(original, 1, 0, create_color(1, 2, 14))
    set_color(original, 2, 0, create_color(1, 3, 13))
    set_color(original, 3, 0, create_color(1, 4, 12))
    set_color(original, 4, 0, create_color(1, 5, 11))

    set_color(original, 0, 1, create_color(1, 6, 10))
    set_color(original, 1, 1, create_color(1, 7, 9))
    set_color(original, 2, 1, create_color(1, 8, 8))
    set_color(original, 3, 1, create_color(1, 9, 7))
    set_color(original, 4, 1, create_color(1, 10, 6))
    set_color(original, 0, 2, create_color(1, 11, 5))
    set_color(original, 1, 2, create_color(1, 12, 4))
    set_color(original, 2, 2, create_color(1, 13, 3))
    set_color(original, 3, 2, create_color(1, 14, 2))
    set_color(original, 4, 2, create_color(1, 15, 1))

    expected = create_image(5,
                            3)  # Shows the expected values of the pixels after the copy of the original image is put through the filter
    set_color(expected, 0, 0, create_color(1, 5, 11))
    set_color(expected, 1, 0, create_color(1, 4, 12))
    set_color(expected, 2, 0, create_color(1, 3, 13))
    set_color(expected, 3, 0, create_color(1, 2, 14))
    set_color(expected, 4, 0, create_color(1, 1, 15))

    set_color(expected, 4, 1, create_color(1, 6, 10))
    set_color(expected, 3, 1, create_color(1, 7, 9))
    set_color(expected, 2, 1, create_color(1, 8, 8))
    set_color(expected, 1, 1, create_color(1, 9, 7))
    set_color(expected, 0, 1, create_color(1, 10, 6))

    set_color(expected, 4, 2, create_color(1, 11, 5))
    set_color(expected, 3, 2, create_color(1, 12, 4))
    set_color(expected, 2, 2, create_color(1, 13, 3))
    set_color(expected, 1, 2, create_color(1, 14, 2))
    set_color(expected, 0, 2, create_color(1, 15, 1))

    vertical_image = flip_vertical(original)
    for x, y, col, in vertical_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x,
                                   y))  # Prints the location of the filter and whether the pixel PASSED through the filter or FAILED


def test_flip_horizontal() -> None:
    '''A test function for extreme contrast.

    If  flip_horizontal works

    >>> test_flip_horizontal()
    all pixels PASSED

    If  flip_horizontal fails at pixel with coordinates (1,0) where
    the value is (red=0, green=127, blue=1)
    and should be (red=0, green=0, blue=0)

    >>> test_flip_horizontal()
    Checking pixel  at coordinates (0, 0) FAILED: expected
    Color(red=0, green=0, blue=0), got Color(red=0, green=127, blue=1)

    # Author: Orit Hashim
    # Student number: 101142803
    '''

    # This test function checks if  flip_horizontal
    # correctly transforms pixels in orginal:
    # get_color(0,0) to get_color(0, 1)
    # get_color(1, 0) to get_color(1, 1)
    # get_color(2, 0) to get_color(2, 1)
    # get_color(3, 0) to get_color(3, 1)
    # get_color(0, 1) to get_color(0, 0)
    # get_color(1, 1) to get_color(1, 0)
    # get_color(2, 1) to get_color(2, 0)
    # get_color(3, 1) to get_color(3, 0)

    counter = 0
    # create original photo with enough "x" pixels so...
    # that the user can press the "close" button.
    original = create_image(4, 2)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 127, 1))
    set_color(original, 2, 0, create_color(128, 128, 128))
    set_color(original, 3, 0, create_color(12, 128, 12))
    set_color(original, 0, 1, create_color(125, 73, 224))
    set_color(original, 1, 1, create_color(255, 123, 245))
    set_color(original, 2, 1, create_color(25, 27, 89))
    set_color(original, 3, 1, create_color(11, 11, 12))

    # create expected photo after original photo is run though flip_horizontal
    expected = create_image(4, 2)
    set_color(expected, 0, 0, create_color(125, 73, 224))
    set_color(expected, 1, 0, create_color(255, 123, 245))
    set_color(expected, 2, 0, create_color(25, 27, 89))
    set_color(expected, 3, 0, create_color(11, 11, 12))
    set_color(expected, 0, 1, create_color(0, 0, 0))
    set_color(expected, 1, 1, create_color(0, 127, 1))
    set_color(expected, 2, 1, create_color(128, 128, 128))
    set_color(expected, 3, 1, create_color(12, 128, 12))

    flipped_image = flip_horizontal(original)

    # col is the Color object for the pixel @ (x,y)
    for x, y, col in flipped_image:
        description_check_equals = "Checking pixel  at coordinates {}".format((x, y))
        counter += check_equal(description_check_equals,
                               col, get_color(expected, x, y))
        # prints only if there are no discrepancies between the expected image
    # and the image created by flip_horizontal
    if counter == 0:
        print("all pixels PASSED")