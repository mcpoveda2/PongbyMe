from turtle import Turtle,Screen
from paddle import Paddle

screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong by Michael")
screen.tracer(0)

paddle1 = Paddle()

screen.listen()
screen.onkey(fun = paddle1.up, key="Up")
screen.onkey(fun = paddle1.down, key="Down")

game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()