from turtle import Turtle, Screen
from time import sleep
from snake import Snake

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# segments = []
# positions = [(0,0),(-20,0),(-40,0)]

# for position in positions:
#     segment = Turtle(shape="square")
#     segment.penup()
#     segment.setposition(position)
#     segment.color("white")
#     segments.append(segment)

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    # for seg_num in range(len(segments)-1, 0, -1):
    #     new_x = segments[seg_num-1].xcor()
    #     new_y = segments[seg_num-1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segments[0].forward(20)







screen.exitonclick()
