from turtle import Turtle, setheading

STARTING_POSITION = (-250, -280)
INNER_FORWARD = 500
OUTER_FORWARD = 540


class BeautifulBorders():
    def __init__(self):
        self.designer = Turtle(shape="square")
        self.designer.penup()
        self.designer.goto(-250, -250)
        self.designer.pendown()
        self.designer.hideturtle()
        self.designer.color("blue")
        self.designer.setheading(0)
        for _ in range(13):
            self.designer.forward(INNER_FORWARD)
            self.designer.setheading(90)
            self.designer.forward(20)
            self.designer.setheading(180)
            self.designer.forward(INNER_FORWARD)
            self.designer.setheading(90)
            self.designer.forward(20)
            self.designer.setheading(0)
        self.designer.setheading(180)
        self.designer.forward(20)
        self.designer.setheading(270)
        self.designer.forward(540)
        self.designer.setheading(0)
        self.designer.forward(OUTER_FORWARD)
        self.designer.setheading(90)
        self.designer.forward(560)
        self.designer.setheading(180)
        self.designer.forward(OUTER_FORWARD)