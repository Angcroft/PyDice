# PyDice: CLI Dice Simulator in Python

## Introduction

PyDice is a command-line interface (CLI) application written in Python for simulating dice rolls. This project was created to learn about Python and is made public for those who are also interested in this programming language and want to understand some of its syntax. PyDice is ideal for Python learners as it offers a simple yet functional example of CLI application development.

## Features

To run this project, you'll need Python installed on your system. The project was developed using Python 3.9, so it should work with most recent versions of Python.

## Project Structure

The project consists of the following files:
- `pydice.py`: Contains the main logic and CLI interaction.
- `dices.py`: Implements the dice rolling logic.

## Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Angcroft/PyDice.git
    ```

2. **Navigate to the project directory:**
    ```sh
    cd PyDice
    ```

3. **Run the application:**
    ```sh
    python pydice.py
    ```

## How It Works

When you run the program, you'll see the main prompt asking for the type of dice and the number of rolls.

### User Input

1. **Select Dice Type:** Choose from available dice types such as D6, D20, etc.
2. **Enter Number of Rolls:** Specify how many times you want to roll the selected dice.

### Example Usage

- The program displays all available dice types and prompts you to select one.
- Enter the number of times you want to roll the dice.
- The results of each roll are displayed, followed by the total sum of all results.

## Examples

### Basic Dice Rolling
```sh
All available dice:
D4
D6
D8
D10
D12
D20
D60
D100

Input the desired type of dice (e.g., D6, D20): D6
Input how many rolls you want to make: 5
Results of rolling 5 dice(s) with 6 faces:
Roll 1: 4
Roll 2: 2
Roll 3: 6
Roll 4: 1
Roll 5: 5
Total of all results: 18
```

## Project Files

**pydice.py**

This file contains the main program logic, including user interaction and input validation

```sh
from dices import DICE, roll_dice, roll_multiple_dice

def show_dice_options():
    print("All available dice:")
    for dice_option in DICE:
        print(dice_option)

def input_user():
    while True:
        show_dice_options()
        dice_type = input("Input the desired type of dice (e.g., D6, D20): ").upper()
        if dice_type not in DICE:
            print(f"Type of dice '{dice_type}' is not valid. Try again.")
            continue

        try:
            num_rolls = int(input("Input how many rolls you want to make: "))
            if num_rolls > 0:
                return DICE[dice_type], num_rolls
            print("The number of rolls must be a positive integer.")
        except ValueError:
            print("Invalid input. Please, enter integer numbers.")

def main():
    faces, num_rolls = input_user()
    results = roll_multiple_dice(faces, num_rolls)
    
    print(f"Results of rolling {num_rolls} dice(s) with {faces} faces:")
    for i, result in enumerate(results, start=1):
        print(f"Roll {i}: {result}")
    print(f"Total of all results: {sum(results)}")

if __name__ == "__main__":
    main()
```

**dices.py**

This file contains the logic for simulating the dice rolls

```sh
import random

DICE = {
    'D4': 4,
    'D6': 6,
    'D8': 8,
    'D10': 10,
    'D12': 12,
    'D20': 20,
    'D60': 60,
    'D100': 100,
}

def roll_dice(faces):
    return random.randint(1, faces)

def roll_multiple_dice(faces, num_rolls):
    return [roll_dice(faces) for _ in range(num_rolls)]
```
## About the Use of this Project

This project is open for contributions. Feel free to fork the repository and make improvements. Any beneficial use of the code is permitted in accordance with the MIT License.
