from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong by Michael")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle1 = Paddle((-350,0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun = r_paddle.up, key="Up")
screen.onkey(fun = r_paddle.down, key="Down")

screen.onkey(fun = l_paddle1.up, key="w")
screen.onkey(fun = l_paddle1.down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if(ball.ycor()>=280 or ball.ycor()<=-280):
        ball.bounce_y()
        
    #Detect collision with r_paddle

    if(ball.distance(r_paddle)<50 and ball.xcor()>320):
        ball.bounce_x()

    # Detect collision with l_paddle
    if (ball.distance(l_paddle1) < 50 and ball.xcor() < -320):
        print("chitoi")
        ball.bounce_x()

    # Detect when right paddle misses
    if(ball.xcor()>360):
        ball.reset_position()
        scoreboard.increseDerecha()

    if(ball.xcor()<-360):
        ball.reset_position()
        scoreboard.increseIzquierda()


screen.exitonclick()