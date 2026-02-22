from turtle import Turtle

Font = ("Arial", 8, "bold")

class Write(Turtle):
    def __init__(self, province, position):
        super().__init__()
        self.shape("turtle")
        self.goto(position)
        self.write(province, font=Font)