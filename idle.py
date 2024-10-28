#상태를 쿨래스를 통해서 정의함.
class Idle:
    @staticmethod   #@는 데코레이드 같은 기능
    def enter():
        pass
    @staticmethod
    def exit():
        pass
    @staticmethod
    def do():
        pass
    @staticmethod
    def draw():
        pass