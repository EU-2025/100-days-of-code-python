# import colorgram
from turtle import Turtle, Screen, colormode
from random import choice

# color_list = []
# colors = colorgram.extract('image.jpg', 16)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r,g,b))
# print(color_list)

colormode(255)

screen = Screen()
width = 800
height = 600
screen.setup(width, height)

tortuga = Turtle()
tortuga.hideturtle()
tortuga.speed("fastest")
# dot_amout = 800/(2*100)

color_list = [
    # (253, 253, 252), 
    # (242, 244, 247), 
    # (241, 247, 243), 
    (144, 76, 50), 
    (188, 165, 117), 
    # (248, 244, 246), 
    (166, 153, 36), 
    (14, 46, 85), 
    (139, 185, 176), 
    (146, 56, 81), 
    (42, 110, 136), 
    (59, 120, 99), 
    (145, 170, 177), 
    (87, 35, 30), 
    (64, 152, 169), 
    (220, 209, 93)
    ]

size = 30 # multiplos de width and height
x = ((width/2)*(-1)) + size/2 + 10
y = ((height/2)*(-1)) + size/2 + 10

while y < (((height/2)- size/2) + 10):
    while x < (((width/2)- size/2) + 10):
        # tortuga.color(choice(colors).rgb)
        # tortuga.color(choice(color_list))
        tortuga.penup()
        tortuga.goto(x, y)
        tortuga.pendown()
        tortuga.dot(size, choice(color_list))
        x += 2*size
    y += 2*size
    x = ((width/2)*(-1)) + size/2 + 10

print(screen.screensize())
screen.exitonclick()