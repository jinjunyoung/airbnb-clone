class Dog:
    def __init__(self):
        print("woof woof")

    def pee(self):
        print("i will pee")


class Puppy(Dog):
    def pee(self):
        print("go to the park")
        super().pee()


p = Puppy()
p.pee()