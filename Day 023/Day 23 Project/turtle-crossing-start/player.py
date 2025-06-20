from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.shapesize(1.25, 1.25)
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def restart_game(self):
        self.goto(STARTING_POSITION)
    
    def go_up(self):
        if self.ycor()<=FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)
    

