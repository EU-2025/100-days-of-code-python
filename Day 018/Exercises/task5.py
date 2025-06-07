from turtle import Turtle, Screen, colormode
from random import choice, randint

# turtle_colors = [
#     "white", "black", "gray", "red", "green", "blue", "cyan", "yellow", "magenta",
#     "orange", "purple", "brown", "pink", "gold", "silver", "navy", "turquoise",
#     "lime", "maroon", "olive", "teal", "aqua", "coral", "indigo", "violet"
# ]

def random_color(tortuga):
    colormode(255)
    tortuga.color((randint(0, 255), randint(0, 255), randint(0, 255)))

def drawing_n_polygons(tortuga, number, side_length, rand_color):
    for sides in range(3, number+1):
        if rand_color:
            random_color(tortuga) 
        else:
            tortuga.color("black")
        total_lines = 0
        while total_lines < sides:
            tortuga.forward(side_length)
            tortuga.right(360/sides)
            total_lines += 1

t = Turtle()

drawing_n_polygons(t, 6, 120, True)

screen = Screen()
screen.exitonclick()