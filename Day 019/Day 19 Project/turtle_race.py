from turtle import Turtle, Screen
import random as rd

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
print(f"Your guess is: {user_bet}\n Good luck!\n")
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
tortugas = []
y_coord = 150
x_coord = -230

pencil = Turtle()
pencil.speed("fastest")
pencil.penup()
pencil.goto(x = 225, y = 170)
pencil.pendown()
pencil.goto(x = 225, y = -170)
pencil.hideturtle()
pencil.ycor

del pencil

for color in colors:
    new_turtle = Turtle(shape = "turtle")
    new_turtle.speed("fastest")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x_coord,  y_coord)
    tortugas.append(new_turtle)
    y_coord -= 50

if user_bet:
    is_race_on = True

while is_race_on:
    for tortuga in tortugas:
        if round(tortuga.xcor()) >= 225:
            is_race_on = False
            winner = tortuga.pencolor()
            if user_bet.lower() == winner:
                print(f"Congratulations! The winner is {winner}. You've guessed it!")
            else:
                print(f"The winner is {winner}. You lose :c")
        distance = rd.randint(1,15)
        tortuga.forward(distance)
    
screen.exitonclick()
