from dices import DICE, rollMultipleDices

def showDices():
    print("All available dices: ")
    for diceOptions in DICE:
        print(diceOptions)

def input_user():
    while True:
        showDices()
        diceType = input("Input the desired faces of dice: ").upper()
        if diceType not in DICE:
            print(f"Type of dice '{diceType}' is not valid. Try again.")
            continue


        try:
            numroll = int(input("Input how many rolls you want to make: "))
            if numroll > 0:
                return DICE[diceType], numroll
            print("The number of rolls must be a positive integer.")
        except ValueError:
            print("Invalid input. Please, enter integer numbers.")

def main():
    faces, numroll = input_user()
    results = rollMultipleDices(faces, numroll)
    
    print(f"Results of rolling {numroll} dice(s) with {faces} faces: ")
    for i, result in enumerate(results, start=1):
        print(f"Rolling {i}: {result}")
    print(f"Total of all results: {sum(results)}")

if __name__ == "__main__":
    main()