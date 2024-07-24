from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        #self.speed("fastest")
        self.goto(position[0], position[1])

    def up(self):
        ycor = self.ycor() + 20
        self.goto(self.xcor(),ycor)

    def down(self):
        ycor = self.ycor() - 20
        self.goto(self.xcor(), ycor)
