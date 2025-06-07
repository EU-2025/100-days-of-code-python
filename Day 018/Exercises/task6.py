from turtle import Turtle, Screen, colormode
from random import choice, randint

t = Turtle()

def random_color(tortuga):
    colormode(255)
    tortuga.color((randint(0, 255), randint(0, 255), randint(0, 255)))

def walk_randomly_n_steps(tortuga, distance, steps):
    tortuga.pensize(10)
    turnings = [0, 90 , -90, 180]
    for step in range(0, steps):
        tortuga.right(choice(turnings))
        random_color(tortuga)
        tortuga.forward(distance)
        tortuga.speed("fastest")
    
walk_randomly_n_steps(t, 25, 100)

screen = Screen()
screen.exitonclick()