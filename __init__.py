from matrix import colors
from matrix import buttons
from matrix import networking
from matrix import random
from matrix import time

def put_pixel(x, y, color):
    from bridge import set_pixel_color
    set_pixel_color((16 * x) + y, color.red, color.green, color.blue)

def fill(color):
    from bridge import fill_pixels_color
    fill_pixels_color(color.red, color.green, color.blue)