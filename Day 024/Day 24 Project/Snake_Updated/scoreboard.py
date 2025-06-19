from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = ''
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.read_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_board(self):
        if self.score > self.high_score:
            self.update_high_score()
            self.read_high_score()
            
        self.score = 0
        self.update_scoreboard()
        
    def read_high_score(self):
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
    
    def update_high_score(self):
        with open("high_score.txt",mode="w") as file:
            file.write(str(self.score))
            

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
