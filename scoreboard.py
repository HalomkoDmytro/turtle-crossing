from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT_SCORE = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score_board()

    def update_score_board(self):
        self.score += 1
        self.clear()
        self.goto(-240, 280)
        self.write(f"Score: {self.score}",
                   align="center",
                   font=FONT_SCORE)

    def game_over(self):
        self.clear()
        self.goto(-20, 20)
        self.write(f"GAME OVER\nScore: {self.score}",
                   align="center",
                   font=FONT)
