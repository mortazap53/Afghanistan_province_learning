# 🇦🇫 Afghanistan Provinces Guessing Game
A simple Python geography game built with **Turtle** and **Pandas** where players try to guess all **34 provinces of Afghanistan**. Correct guesses are displayed on the map in their corresponding locations.

## Features
- 🗺️ Interactive map of Afghanistan
- ✍️ Enter province names through a pop-up dialog
- ✅ Correct guesses are displayed on the map
- 📊 Tracks your progress (e.g., `10/34`)
- 🚪 Type `Exit` to quit the game
- 📋 Prints all unguessed provinces when the game ends

## Technologies Used
- Python 3
- Turtle
- Pandas

## Project Structure
```text
.
├── main.py
├── writing_name.py
├── Afghanistan_provinces.csv
├── AFG map.gif
└── README.md
```

## Requirements
Install the required package:

```bash
pip install pandas
```

## How to Run
1. Clone or download this repository.
2. Make sure all project files are in the same directory.
3. Run the program:

```bash
python main.py
```

## How to Play
1. A map of Afghanistan will appear.
2. Enter the name of a province in the input box.
3. If your answer is correct, the province name will be displayed on the map.
4. Continue until you guess all 34 provinces or type `Exit` to quit.
5. After exiting, the program prints a list of all provinces you did not guess.

## Data Files
- **Afghanistan_provinces.csv** – Contains the province names and their `(x, y)` coordinates.
- **AFG map.gif** – Background map displayed in the game.
- **writing_name.py** – Handles writing province names on the map.

## Future Improvements
- Save missed provinces to a CSV file for later practice.
- Add a timer or countdown.
- Track high scores.
- Accept alternative spellings.
- Improve the user interface with animations and sound effects.

## Known Issue
The following line in the code:

```python
if guessing_province in Provinces not in guessed_provinces:
```

should be replaced with:
```python
if guessing_province in Provinces and guessing_province not in guessed_provinces:
```

This ensures the program correctly checks that the province exists and has not already been guessed.

## Author
**Mortaza Panahi**
