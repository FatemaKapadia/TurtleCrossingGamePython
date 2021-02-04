from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]



class CarManager:

    def __init__(self):
        self.cars = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10

    def newCar(self):
        if random.randint(1, 6)==1 :
            x1 = Turtle()
            x1.penup()
            x1.goto(300, random.randrange(-200, 200, 10))
            x1.color(random.choice(COLORS))
            x1.shape("square")
            x1.shapesize(stretch_len=2)
            x1.setheading(180)
            self.cars.append(x1)

    def moveCars(self):
        for i in self.cars:
            i.forward(self.STARTING_MOVE_DISTANCE)
            if i.xcor() == -300:
                newpos = (300, random.randrange(-200, 200, 10))
                i.goto(newpos)
                i.color(random.choice(COLORS))

    def isSafe(self, player):
        for i in self.cars:
            if player.distance(i) <= 17:
                return False
        return True

    def increaseSpeed(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT
