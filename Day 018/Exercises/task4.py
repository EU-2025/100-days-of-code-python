from turtle import Turtle, Screen

tortuga = Turtle()
tortuga.shape("turtle")

total_distance = 0
line = 10
while total_distance < 300:
    tortuga.color("green")
    tortuga.forward(line)
    tortuga.penup()
    # tortuga.color("white")
    tortuga.forward(line)
    tortuga.pendown()
    # tortuga.color("green")
    total_distance += 2*line

screen = Screen()
screen.exitonclick()