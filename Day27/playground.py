def add(*args):
    total = 0
    for n in args:
        total += n
    return total


total = add(1, 2)
print(total)


def calc(**kwargs):
    print(kwargs)


calc(add=1, mul=2)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


mycar = Car(make="Mitsubishi", model="Lan Evo 6")
print(mycar.make)
