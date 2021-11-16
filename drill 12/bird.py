import random
from pico2d import *
import game_world
import game_framework


# Bird Run Speed
PIXEL_PER_METER = (100.0 / 0.14)  # 100 pixel 14 cm  새는 참새라 가정 한국민족문화대백과 기준 14cm크기의 소형 조류
RUN_SPEED_KMPH = 8.0  # Km / Hour   검색 결과 시속 180km/h라고 한다.. ?
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 0.5 # 초당 날개짓 회수는 못찾음
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x = random.randint(50, 1600-50)
        self.y = random.randint(450, 600-50)
        self.dir = random.randint(0, 1)
        self.frame = random.randint(0, 14)
        print('생성됨', self.dir)

    def get_bb(self):
        # fill here
        return 0,0,0,0

    def draw(self):
        # print(self.x, self.dir, RUN_SPEED_PPS * game_framework.frame_time)
        if self.dir == 0:
            self.image.clip_draw(int(self.frame) * 100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

        if self.dir == 0:
            self.x -= RUN_SPEED_PPS * game_framework.frame_time
        else:
            self.x += RUN_SPEED_PPS * game_framework.frame_time

        if self.x > 1600 - 50:
            self.dir = 0
            # self.x = 1600 - 51
        elif self.x < 50:
            # self.x = 51
            self.dir = 1





