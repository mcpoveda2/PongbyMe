from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0,0)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.speed_x = 10
        self.speed_y = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor()
        y = self.ycor()

        self.setx(x+self.speed_x)
        self.sety(y+self.speed_y)


    def bounce_y(self):
        self.speed_y *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.speed_x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()