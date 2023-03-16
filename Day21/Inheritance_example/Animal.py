class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("inhale, exhalte")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("Underwater")

    def swim(self):
        print("Swim")


nemo = Fish()
nemo.swim()
nemo.breath()
