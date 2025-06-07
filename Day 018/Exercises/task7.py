from turtle import Turtle, Screen, colormode
from random import choice, randint

tortuga = Turtle()
colormode(255)

def random_color():
    return (randint(0,255), randint(0,255), randint(0,255))

radius = 100
distance_in_degrees = 5 # Choose multiples of 360 degrees
number_of_circles = round(360/distance_in_degrees)
# tortuga.color(random_color())

for movement in range(number_of_circles):
    tortuga.color(random_color())
    tortuga.speed("fastest")
    tortuga.circle(radius)
    tortuga.right(distance_in_degrees)

screen = Screen()
screen.exitonclick()
