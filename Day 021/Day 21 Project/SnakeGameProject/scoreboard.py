from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier',14,"bold")

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(x=0, y=280)
        self.write(f"Score: {self.score}", False, align="center", font = ('Arial',14,"bold"))
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", False, align="center", font = ('Arial',14,"bold"))
    
    def update(self):
        self.clear()
        self.score +=1
        self.write(f"Score: {self.score}",False, align=ALIGNMENT, font = FONT)