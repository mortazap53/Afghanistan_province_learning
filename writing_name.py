from turtle import Turtle

Font = ("Arial", 8, "bold")

class Write(Turtle):
    def __init__(self, province, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(arg=province, font=Font)