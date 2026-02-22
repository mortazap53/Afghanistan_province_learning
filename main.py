from turtle import Turtle, Screen
from writing_name import Write
import pandas

screen = Screen()
Turtle = Turtle()
screen.setup(width=800, height=600)
image = "AFG map.gif"
screen.addshape(image)
Turtle.shape(image)

data = pandas.read_csv("Afghanistan_provinces.csv")
Provinces = data.provinces.tolist()

guessed_provinces = []
while len(guessed_provinces) < len(Provinces):
    guessing_province = screen.textinput(f"{len(guessed_provinces) + 1}/{len(Provinces)} Guess a province",
                                        "Write name of a province").title()
    if guessing_province == "Exit":
        break
    if guessing_province in Provinces not in guessed_provinces:
        guessed_provinces.append(guessing_province)
        row = data[data.provinces == guessing_province]
        xcor = row.x.item()
        ycor = row.y.item()
        Write(guessing_province, (xcor, ycor))

remaining_provinces = []
for province in Provinces:
    if province not in guessed_provinces:
        remaining_provinces.append(province)
print(f"Here is all the remaining provinces:{remaining_provinces}")