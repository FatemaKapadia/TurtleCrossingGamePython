import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
scoreb = Scoreboard()
screen.listen()
cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.onkeypress(fun=tim.move, key="Up")
    cars.newCar()

    if tim.ycor() >= 250:
        tim.reset()
        scoreb.increaseLevel()
        cars.increaseSpeed()

    cars.moveCars()
    game_is_on = cars.isSafe(tim)

    screen.update()

scoreb.gameOver()

screen.exitonclick()
