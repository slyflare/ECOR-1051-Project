from Cimpl import copy, Image, get_color, set_color, show, load_image, create_image, save_as, choose_file, create_color
from simple_Cimpl_filters import grayscale

def sepia(image: Image) -> Image:
    """Returns a new image that is sepia tinted
    
       Code by Marcelo Saldivia-Woo
    """
    
    new_image = image

    grayscale_image = grayscale(new_image)
    
    sepia_tinted = grayscale_image

    for x,y, (r,g,b) in sepia_tinted:     
                          
        if b <= 63 and b > 0:
            sepia1 = create_color(r*1.1, g, b*0.9)
            set_color(sepia_tinted, x,y, sepia1)
        elif r > 63 and r < 191:
            sepia2 = create_color(r*1.15, g, b*0.85)
            set_color(sepia_tinted, x,y, sepia2)
        elif r > 191 and r <= 236:
            sepia3 = create_color(r*1.08, g, b*0.93)
            set_color(sepia_tinted, x,y, sepia3)
        
    return sepia_tinted
