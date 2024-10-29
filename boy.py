from pico2d import load_image, get_time
from sdl2 import SDL_KEYDOWN, SDLK_SPACE

from state_machine import StateMachine, time_out, space_down, right_down, left_up, left_down, right_up, start_event, \
    a_down


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
        self.state_machine.start(Idle) #초기 상태가 Idle
        self.state_machine.set_transitions(
            {
                Idle  : { a_down: AutoRun,right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out : Sleep },
                Run : {right_down: Idle, left_down: Idle, right_up:Idle, left_up:Idle}, # Run 상태에서 어떤 이벤트가 들어와도 처리하지 않겠다.
                AutoRun : {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Idle },
                Sleep : { right_down: Run, left_down: Run, left_up: Run, right_up: Run, space_down : Idle }
            }
        )

    def update(self):
        self.state_machine.undate()

    def handle_event(self, event):
        # event : 입력 이벤트 key mouse
        # 우리가 state machine에게 전달해줄껀 ( , )
        self.state_machine.add_event(('INPUT',event))
        pass

    def draw(self):
        self.state_machine.draw()

#상태를 쿨래스를 통해서 정의함.
class Idle:
    @staticmethod   #@는 데코레이드 같은 기능
    def enter(boy,e):
        if left_up(e) or right_down(e):
            boy.action = 2
            boy.face_dir = -1
        elif right_up(e) or left_down(e) or start_event(e):
            boy.action = 3
            boy.face_dir = 1
        boy.dir = 0 #정지 상태
        boy.frame = 0
        # 현재 시간을 저장
        boy.start_time = get_time()
        pass
    @staticmethod
    def exit(boy,e):
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1)%8
        if get_time() - boy.start_time > 3:
            boy.state_machine.add_event(('TIME_OUT', 0))
        pass
    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)
        pass

class Sleep:
    @staticmethod
    def enter(boy,e):
        pass
    @staticmethod
    def exit(boy,e):
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame+1)%8
        pass
    @staticmethod
    def draw(boy):
        if boy.face_dir ==1: #오른쪽 바라본 상태에서 눕기
            boy.image.clip_composite_draw(
                boy.frame*100,300,100,100,3.141592/2, #90회전
                '', #좌우상하 반전X
                boy.x - 25,boy.y - 25,100,100
            )
        elif boy.face_dir ==-1: #왼쪽 바라본 상태에서 눕기
            boy.image.clip_composite_draw(
                boy.frame * 100, 200, 100, 100, -3.141592 / 2,  # 90회전
                '',  # 좌우상하 반전X
                boy.x + 25, boy.y - 25, 100, 100
            )
        pass

class Run:
    @staticmethod
    def enter(boy,e):
        if right_down(e) or left_up(e):
            boy.dir,boy.face_dir,boy.action=1,1,1
        elif left_down(e) or right_up(e):
            boy.dir,boy.face_dir,boy.action=-1,-1,0
    @staticmethod
    def exit(boy,e):
        pass
    @staticmethod
    def do(boy):
        boy.frame=(boy.frame+1)%8
        boy.x += boy.dir * 5
        pass
    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame*100,boy.action*100,100,100,boy.x,boy.y)

class AutoRun:
    @staticmethod
    def enter(boy,e):
        if boy.face_dir==1:
            boy.dir,boy.action=1,1
        elif boy.face_dir==-1:
            boy.dir,boy.action=-1,0
        boy.start_time = get_time()
        pass
    @staticmethod
    def exit(boy,e):
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.x += boy.dir * 10
        if get_time() - boy.start_time > 5:
            boy.state_machine.add_event(('TIME_OUT', 0))
        pass
    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y+25,150,150)
        pass