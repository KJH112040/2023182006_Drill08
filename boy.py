from pico2d import load_image
from state_machine import StateMachine

class Boy:
    image = None
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 0
        self.action = 3
        if Boy.image==None:
            self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine()
        self.state_machine.start()

    def update(self):
        self.frame = (self.frame + 1) % 8

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.action * 100, 100, 100, self.x, self.y)
