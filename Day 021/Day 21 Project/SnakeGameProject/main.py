from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collisiom with food.
    if snake.head.distance(food) < 15:
        # The distance is 15, because turtle is 20*20 and food 10*10
        # print("nom nom nom")
        food.refresh()
        snake.grow()
        scoreboard.update()
    
    # Detect collition with the wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    
    # Detect collition with tail.
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            game_is_on = False
            scoreboard.game_over()







screen.exitonclick()

