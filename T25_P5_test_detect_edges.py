# ECOR 1051
# Coded by Marcelo Saldivia-Woo
# March 24, 2020

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_color, create_image, \
    save_as, save, get_height, get_width

from T25_filter_edge_detection import detect_edges


def check_equal(description: str, outcome, expected) -> int: # original function written by Professor Cheryl Schramm, edited by teammate Orit Hashim

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
        

def test_detect_edges():
    # Code is taken from Professor Cheryl Schramm, edited by Marcelo Saldivia-Woo
    # This test function checks if the detect_edges filter will iterate properly over the given image
    original = create_image(3, 2)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 0, 1,  create_color(128, 128, 128))
    set_color(original, 1, 0,  create_color(60, 120, 60))
    set_color(original, 1, 1,  create_color(255, 255, 255))
    set_color(original, 2, 0,  create_color(140, 0, 140))
    set_color(original, 2, 1,  create_color(0, 150, 150))

    # Create an image that's identical to the one a correct implementation of
    # detect_edges should produce when it is passed original.

    expected = create_image(3, 2)
    set_color(expected, 0, 0,  create_color(255, 255, 255))
    set_color(expected, 0, 1,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(255, 255, 255))
    set_color(expected, 1, 1,  create_color(0, 0, 0))
    set_color(expected, 2, 0,  create_color(255, 255, 255))
    set_color(expected, 2, 1,  create_color(255, 255, 255))
   
    detect_edges_trial = detect_edges(original, 12)
    check = 0
    problem = 0
    for x, y, col in detect_edges_trial:  # col is the Color object for the pixel @ (x,y).
        check += check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))
        if check !=0 : # this will compare the expected values with the detect_edges function's output of the original values
            problem += 1   # this indicates that there are inconsistent values between expected and the detect_edges function
        print ("pixel at {}".format ((x,y)), "PASSED")


test_detect_edges()   #Calls the function test_detect_edges()