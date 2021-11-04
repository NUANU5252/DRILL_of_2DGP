from pico2d import *

# Boy Event
# fill here
RIGHT_DOWN, LEFT_DOWN, LSHIFT_DOWN, RIGHT_UP, LEFT_UP, LSHIFT_UP, SLEEP_TIMER = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_LSHIFT): LSHIFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_LSHIFT): LSHIFT_UP
}


# Boy States
class IdleState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.timer = 1000

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)


class RunState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1

        if boy.velocity > 0:
            boy.dir = 1
        elif boy.velocity == 0:
            boy.dir = 0
        else:
            boy.dir = -1

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


class SleepState:
    def enter(boy, event):
        boy.frame = 0

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)

class DashState:
    def enter(boy, event):

        if event == LSHIFT_DOWN:
            boy.velocity *= 2

        if boy.velocity > 0:
            boy.dir = 1
        elif boy.velocity == 0:
            boy.dir = 0
        else:
            boy.dir = -1

        boy.dash_timer = 100
        boy.is_dashing = True

    def exit(boy, event):
        if boy.is_dashing == True:
            boy.velocity /= 2
        boy.is_dashing = False

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)
        boy.dash_timer -= 1
        if boy.dash_timer == 0:
            boy.add_event(LSHIFT_UP)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, LSHIFT_UP: IdleState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState, LSHIFT_DOWN: IdleState,
                SLEEP_TIMER: SleepState},

    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LSHIFT_UP: RunState,
               RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState, LSHIFT_DOWN: DashState},

    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LSHIFT_DOWN: SleepState,
                 LEFT_UP: RunState, RIGHT_UP: RunState, LSHIFT_UP: SleepState},

    DashState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LSHIFT_UP: RunState,
               RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState, LSHIFT_DOWN: DashState},
}


class Boy:

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        # fill here
        self.frame = 0
        self.timer = 0
        self.dash_timer = 0

        self.is_dashing = False

        self.event_que = []

        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def change_state(self,  state):
        # fill here
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):

        self.cur_state.do(self)

        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + ' Dir:' + str(self.dir) + 'Cur_state : ' + str(self.cur_state))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)