from random import randint
class Die:

    def __init__(self, sides = 6):
        self.sides = sides
    def roll_die(self):
        print(f"The die rolled and stopped at:\n {randint(1,self.sides)}")
