from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level= 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.display_scoreboard()
        
    def increase_level(self):
        self.level += 1
        self.display_scoreboard()
    
    def display_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def game_over(self):
        self.goto(0, -250)
        self.write(f"GAME OVER! \nYou got hit!", align="center", font=FONT)
