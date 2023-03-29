from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)

screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()



screen.listen()
screen.onkeypress(paddle1.go_up,"Up")
screen.onkeypress(paddle1.go_down,"Down")
screen.onkeypress(paddle2.go_up,"w")
screen.onkeypress(paddle2.go_down,"s")


game_is_on = True

while game_is_on:

    time.sleep(ball.pace)
    screen.update()
    ball.move()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()