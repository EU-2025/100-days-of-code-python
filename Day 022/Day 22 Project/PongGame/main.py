from turtle import Turtle, Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong The Game")
screen.tracer(0)

l_paddle = Paddle(-350)
r_paddle = Paddle(350)
pong_ball = Ball()
score = Scoreboard()


screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    screen.update()
    pong_ball.move()
    sleep(0.1)
    
    # Detect collition with wall.
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()
        
    # Detect collition with right paddle.
    if (pong_ball.distance(r_paddle)<50 and pong_ball.xcor() >320) or (pong_ball.distance(l_paddle)<50 and pong_ball.xcor() <-320):
        pong_ball.bounce_x()
    
    # Detect when right paddle misses
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        score.l_point()
    
    # Detect when left paddle misses
    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        score.r_point()
screen.exitonclick()
