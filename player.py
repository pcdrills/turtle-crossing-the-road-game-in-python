from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        # self.get_info()
        self.go_to_start()
    
    # Move the turtle up the screen by 10 pixels
    def go_up(self):
        self.forward(MOVE_DISTANCE)
    
    #Check if the turtle is at the finish line on the y-axis
    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
        
    # def get_info(self):
    #     name = self.textinput()
    #     print(self.name)
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)
        
        