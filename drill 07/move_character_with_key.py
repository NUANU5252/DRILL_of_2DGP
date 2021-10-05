from pico2d import *


def handle_events():
    global running
    global dir_
    global speed
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir = 2
                speed += 1
            elif event.key == SDLK_LEFT:
                dir = 1
                speed -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                speed -= 1
            elif event.key == SDLK_LEFT:
                speed += 1

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0
dir_ = 2 # 방향 1 = left 2 right
speed = 0 # x축의 속도 양수 right 음수 left
status = 0 # 0 : 우측 기본, 1 : 좌측 기본, 2 : 우측 이동, 3 : 좌측 이동

while running:
    clear_canvas()
    grass.draw(400, 30)
    if speed > 0:
        status = 1
    elif speed < 0:
        status = 0
    else:
        status = dir_ + 1
    character.clip_draw(frame * 100, 100 * status, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += speed * 5
    delay(0.01)

close_canvas()

