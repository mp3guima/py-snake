import os
from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        try:
            with open("data.txt", "r") as file:
                self.high_score = int(file.read())
        except IOError:
            with open("data.txt", "w") as file:
                self.high_score = 0
                file.write(f"{self.high_score}")
        self.game_is_on = True
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.goto(-10, 280)
        self.clear()
        score_text = f"Score: {self.current_score}   High Score: {self.high_score}"
        self.write(score_text, move=False, align="center", font=("Arial", 14, "normal"))

    def reset_score(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.current_score = 0
        self.refresh_scoreboard()

    def score_up(self):
        self.current_score += 1
        self.refresh_scoreboard()

    def game_over(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.current_score = 0
        self.refresh_scoreboard()
        with open("data.txt", "w") as file:
            file.write(f"{self.high_score}")
        score_text = f"GAME OVER!"
        self.goto(-5, 0)
        self.write(score_text, move=False, align="center", font=("Arial", 22, "normal"))

    def end_game(self):
        self.game_is_on = False