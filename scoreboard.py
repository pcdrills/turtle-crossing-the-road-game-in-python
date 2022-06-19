from turtle import Turtle
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self, gamer):
        super().__init__()
        self.level= 1
        self.point_increment = 1 
        self.points = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.gamer = gamer
        self.display_scoreboard()
    
    #Check and Increase the level on the scoreboard
    def increase_level(self):
        self.level += 1
        self.display_scoreboard()
        
    #Check and increase the points on the scoreboard
    def increase_points(self):
        adder = self.point_increment * self.level
        self.points += adder
        self.display_scoreboard()
    
    #Display the scoreboard itself
    def display_scoreboard(self):
        self.clear()
        self.write(f"Gamer: {self.gamer} Level: {self.level} Points: {self.points}", align="center", font=FONT)
    
    #Game over display 
    def game_over(self):
        self.goto(0, -250)
        self.write(f"GAME OVER! \nYou got hit!", align="center", font=FONT)
