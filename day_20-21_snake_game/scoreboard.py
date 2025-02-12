from turtle import Turtle
TEXT_ALIGN = "center"
FONT = ("Arial", 14, "bold")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt",mode='r+') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score {self.high_score}", False, TEXT_ALIGN, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", False, TEXT_ALIGN, FONT)


    def add_score(self):
        self.score += 1
        self.update_scoreboard()
    
