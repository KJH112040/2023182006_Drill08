class StateMachine:
    def __init__(self,obj):
        self.obj = obj # 어떤 객체를 위한 상태 머신인지 알려줌.

    def start(self,state):
        self.cur_state = state #시작 상태를 받아서, 그걸로 현재 상태를 정의.

    def undate(self):
        self.cur_state.do(self.obj) #Idle.do()

    def draw(self):
        self.cur_state.draw(self.obj)