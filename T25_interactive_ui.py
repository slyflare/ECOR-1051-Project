# ECOR 1051
# DATE SUBMITTED: APRIL 1ST, 2020
# AUTHOR 1: ORIT HASHIM --- 101142803
# AUTHOR 2: VIMAL GUNASEGARAN -- 101155249

# TITLE: INTERACTIVE FILTER FILE
# ---------------------

from T25_image_filters import *

menu_on = True

# this is the default value for "image" and
# indicates that the user has not loaded and image yet
image = 0

# This list does not include L because it is used when checking
# if a user selects these input before selecting L
excepted_inputs = ["S", "2", "3", "X", "T", "P", "E", "I", "V", "H", "Q"]


def menu() -> None:
    """ Prints the menu of the interactive file.

    >>> menu()

    L)oad image   S)ave-as
    2)-tone 	  3)-tone      X)treme contrast   T)int sepia    P)osterize
    E)dge detect  I)mproved edge detect V)ertical flip     H)orizontal flip
    Q)uit

    Author: Orit Hashim, 101142803
    """
    # The following line prints the menu
    print("L)oad image \t S)ave-as \n2)-tone \t 3)-tone\
          \tX)treme contrast \tT)int sepia  \t P)osterize\
          \nE)dge detect \t I)mproved edge detect \tV)ertical flip\
          H)orizontal flip \nQ)uit \n\n", end="")


while menu_on:

    menu()

    # This makes input_val the uppercase version of itself
    input_val = (input(": ")).upper()

    if input_val == "L":
        print('Choose your image file')
        image = load_image(choose_file())
        show(image)

    elif input_val == "S" and image != 0:
        name = input('Name of file (with extention): ')
        # If the user does not enter an extension, the image
        # will automatically be saved as a jpg
        if '.' not in name:
            name = name + '.jpg'
        print('Saving image')
        save_as(image, name)


    # This team had enough time to allow the user to choose their
    # colour values. The colours are constants in the filters
    # module.
    elif input_val == "2" and image != 0:
        colour1 = [255, 255, 0]
        colour2 = [0, 255, 255]
        image = two_tone(image, colour1, colour2)
        show(image)

    elif input_val == "3" and image != 0:

        colour1 = [255, 255, 0]
        colour2 = [255, 0, 255]
        colour3 = [0, 255, 255]
        image = three_tone(image, colour1, colour2, colour3)
        show(image)

    elif input_val == "X" and image != 0:
        image = extreme_contrast(image)
        show(image)

    elif input_val == "T" and image != 0:
        image = sepia(image)
        show(image)

    elif input_val == "P" and image != 0:
        image = posterize(image)
        show(image)

    elif input_val == "E" and image != 0:
        threshold = int(input('Set the threshold: '))
        image = detect_edges(image, threshold)
        show(image)

    elif input_val == "I" and image != 0:
        threshold = int(input('Set the threshold: '))
        image = detect_edges_better(image, threshold)
        show(image)

    elif input_val == "V" and image != 0:
        image = flip_vertical(image)
        show(image)

    elif input_val == "H" and image != 0:
        image = flip_horizontal(image)

    elif input_val == "Q":
        menu_on = False

    # This loop checks whether the user has not uploaded an image
    # or has selected a filter that does not exist
    elif image == 0:
        counter = 0
        for i in range(len(excepted_inputs)):
            if input_val == excepted_inputs[i]:
                counter = 1
        if counter == 0:
            print("No such command \n")
        else:
            print("No image loaded \n")

    else:
        print("No such command \n")