from turtle import Turtle
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pensize(5)
        self.pencolor("black")
        self.level = 1
        self.write_level()
    pass

    def write_level(self):
        self.goto(-270,255)
        self.write(f"Level: {self.level}",font = FONT)
        
    def update_level(self):
        self.level +=1
        self.clear()
        self.write_level()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font = FONT)
        
    def you_win(self):
        self.goto(0,0)
        self.write(f"YOU WON!",align="center",font = FONT)