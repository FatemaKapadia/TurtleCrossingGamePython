from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-200, 250)
        self.write(move=False, arg=f"Level {self.level}:", align="center", font=FONT)
        self.hideturtle()

    def increaseLevel(self):
        self.clear()
        self.level += 1
        self.write(move=False, arg=f"Level {self.level}:", align="center", font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write(arg="Game Over!", font=FONT, align="center", move=False)