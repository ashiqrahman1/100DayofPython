Class Inheritance

- Inheritance allow us to define a class that inherits all the methods and properties from another class

```
example code

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale,Exhale)


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Swim")

```
