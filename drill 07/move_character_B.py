from pico2d import *
from random import randint

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():  # 키_마 등등 조작 함수
    global running
    global x, y

    events = get_events() # Shadows_name_form_outer_scope
    for event in events:
        if event.type == SDL_Quit:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png  ')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

hand_x = 0
hand_y = 0

dir_ = 1  # 방향 1 : 우측 이동, 0 : 좌측 이동


def reset_hand():
    global hand_x, hand_y
    hand_x = randint(0, KPU_WIDTH)
    hand_y = randint(0, KPU_HEIGHT)


def move_character():
    global x, y, dir_
    if hand_x == x and hand_y == y:
        reset_hand()

    x_ = hand_x - x
    y_ = hand_y - y
    if x_ < 0:
        x_ = x_ * -1
    if y_ < 0:
        y_ = y_ * -1

    if x_ > y_:
        if hand_x > x:
            x += 1
            dir_ = 1
        elif hand_x < x:
            x -= 1
            dir_ = 0

        if hand_y > y:
            y += y_ / x_
        elif hand_y < y:
            y -= y_ / x_
    elif x_ < y_:
        if hand_x > x:
            x += x_ / y_
            dir_ = 1
        elif hand_x < x:
            x -= x_ / y_
            dir_ = 0

        if hand_y > y:
            y += 1
        elif hand_y < y:
            y -= 1


reset_hand()
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * dir_, 100, 100, x, y)

    hand.draw(hand_x, hand_y)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

    # 캐릭터가 손으로 간다.
    move_character()

close_canvas()
