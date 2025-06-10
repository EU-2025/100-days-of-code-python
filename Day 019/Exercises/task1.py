from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)
    
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
# def move_up():
#     tim.setheading(90)
#     move_forward()
    
# def move_down():
#     tim.setheading(270)
#     move_forward()

# def move_left():
#     tim.setheading(180)
#     move_forward()

# def move_right():
#     tim.setheading(0)
#     move_forward()

screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = turn_left)
screen.onkey(key = "d", fun = turn_right)
screen.onkey(key = "c", fun = clear_screen)

# screen.onkey(key = "w", fun = move_up)
# screen.onkey(key = "a", fun = move_left)
# screen.onkey(key = "s", fun = move_down)
# screen.onkey(key = "d", fun = move_right)
screen.exitonclick()

