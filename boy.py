from pico2d import load_image
from state_machine import StateMachine

#상태를 쿨래스를 통해서 정의함.
class Idle:
    @staticmethod   #@는 데코레이드 같은 기능
    def enter():
        pass
    @staticmethod
    def exit():
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1)%8
        pass
    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)
        pass

class Sleep:
    @staticmethod
    def enter():
        pass
    @staticmethod
    def exit():
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame+1)%8
        pass
    @staticmethod
    def draw(boy):
        boy.image.clip_composite_draw(
            boy.frame*100,300,100,100,3.141592/2, #90회전
            '', #좌우상하 반전X
            boy.x - 25,boy.y - 25,100,100
        )
        pass

class Boy:
    image = None
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 0
        self.action = 3
        if Boy.image==None:
            self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine(self) #소년 객체의 state machine 생성
        self.state_machine.start(Sleep) #초기 상태가 Idle

    def update(self):
        self.state_machine.undate()
        # self.frame = (self.frame + 1) % 8

    def handle_event(self, event):
        pass

    def draw(self):
        self.state_machine.draw()
        #self.image.clip_draw(self.frame * 100, self.action * 100, 100, 100, self.x, self.y)
