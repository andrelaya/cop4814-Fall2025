"""
The SimUDuck App - Strategy Design Pattern

Joe works for a company that makes a highly successful duck
pond simulation game, SimUDuck. The game can show a large
variety of duck species swimming and making quacking sounds.
"""

###############################################################################
# Ducks
###############################################################################

# Abstract class Duck
class Duck:
    fly_behavior = None
    quack_behavior = None

    def display(self):
        pass

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()

    def set_quack_behavior(self, new_quack_behavior):
        self.quack_behavior = new_quack_behavior

    def set_fly_behavior(self, new_fly_behavior):
        self.fly_behavior = new_fly_behavior

    def swim(self):
        print("All ducks float, even decoys!!")

class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck")

class DecoyDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    def display(self):
        print("I'm a cute Decoy duck")

class RubberDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self):
        print("I'm the cutest Rubber duck")

class RedHeadDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a dope RedHead duck")


###############################################################################
# Quack behaviors
###############################################################################

class QuackBehavior:
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("Mute")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")

class FakeQuack(QuackBehavior):
    def quack(self):
        print("Cuak")

###############################################################################
# Fly behaviors
###############################################################################
class FlyBehavior():
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly :'(")

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I can fly faster than iron man")


if __name__ == '__main__':
    d1 = MallardDuck()
    d2 = RedHeadDuck()
    d3 = DecoyDuck()

    print(d1, d2, d3)
    d1.fly()
    d1.display()

    d2.display()
    d2.quack()

    d3.display()
    d3.fly()

    d3.set_fly_behavior(FlyRocketPowered())
    d3.fly()

"""
References:
This lecture was designed by Dr Gregory Reis based on the book
Elisabeth Freeman, Eric Freeman, Bert Bates, and Kathy Sierra. 2004
Head First Design Patterns. O' Reilly & Associates, Inc.,
Dr Kip Irvine's class notes, and using the simuduck.py written
by Miguel Alba and modified by Dr Gregory Reis
"""