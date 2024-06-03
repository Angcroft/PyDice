import random

def dice(faces):
    return random.randint(1, faces)

def dice_plural(faces, numroll):
    results = []
    for _ in range(numroll):
        results.append(dice(faces))
    return results

def input_user():
    while True:
        try:
            faces = int(input("Enter the number of faces of dice: "))
            numroll = int(input("Enter the number of rolls: "))
            if faces > 0 and numroll > 0:
                return faces, numroll
            else:
                print("Please, enter positive integers.")
        except ValueError:
            print("Invalid input. Please, enter integer numbers.")

def main():
    faces, numroll = input_user()
    results = dice_plural(faces, numroll)
    print(f"Results of rolling {numroll} dice(s) is {faces} faces: ")
    for i, result in enumerate(results, start=1):
        print(f"Rolling {i}: {result}")
    print(f"Total of all results: {sum(results)}")

if __name__ == "__main__":
    main()