from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def move_rec(x_size = 800, y_size = 600):
    x = 0
    y = 90
    while x < 800:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)

        x += 2

        #delay(0.01)
    while y < 600:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)

        y += 2

        #delay(0.01)
    while x > 0:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)

        x -= 2

        #delay(0.01)
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)

        y -= 2

        #delay(0.01)

def move_circle(center_x = 400, center_y = 300, radius = 300):
    
    degree = 0
    while degree < 360:
        x = sin(degree / 360 * 2 * math.pi) * radius + center_x
        y = cos(degree / 360 * 2 * math.pi) * radius + center_y
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)

        degree += 2

        delay(0.01)
    

while True:
    move_rec()
    move_circle()

close_canvas()
