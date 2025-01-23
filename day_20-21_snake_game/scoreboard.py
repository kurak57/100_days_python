from turtle import Turtle
TEXT_ALIGN = "center"
FONT = ("Arial", 14, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, TEXT_ALIGN, FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, TEXT_ALIGN, FONT)


    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
