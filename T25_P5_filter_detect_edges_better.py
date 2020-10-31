from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_color, create_image, \
    save_as, save, get_height, get_width


def detect_edges_better(image: Image, threshold:int):
    """
    #Coded by Vimal Gunasegaran
    """
    new_image = copy(image)
    for y in range(get_height(new_image)-1):
        for x in range(get_width(new_image)-1):
            r1, g1, b1 = get_color(new_image, x, y)
            r2, g2, b2 = get_color(new_image, x, y + 1)
            r3, g3, b3 = get_color(new_image, x + 1, y)

            con = abs((r1+g1+b1)/3 - (r2+g2+b2)/3)
            con2 = abs((r1+g1+b1/3) - (r3+g3+b3/3))

            if con > threshold:
                set_color(new_image, x, y, create_color(0, 0, 0))
            elif con2 > threshold:
                set_color(new_image, x, y, create_color(0, 0, 0))
            else:
                set_color(new_image, x, y, create_color(255, 255, 255))

    for x in range(get_width(new_image)):
        set_color(new_image, x, get_height(new_image)-1, create_color(255, 255, 255))
    return new_image


show(detect_edges_better(load_image('miss_sullivan.jpg'), 10))