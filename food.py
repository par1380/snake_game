from turtle import Turtle
from random import randint

class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("black")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        self.goto(randint(-300,300),randint(-300,300))


