from turtle import Turtle,Screen
from paddle import Paddle

screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong by Michael")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle1 = Paddle((-350,0))

screen.listen()

screen.onkey(fun = r_paddle.up, key="Up")
screen.onkey(fun = r_paddle.down, key="Down")

screen.onkey(fun = l_paddle1.up, key="w")
screen.onkey(fun = l_paddle1.down, key="s")

game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()