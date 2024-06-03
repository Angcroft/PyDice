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

def rollDice (faces):
    return random.randint(1, faces)

def rollMultipleDices (faces, numroll):
    return [rollDice(faces) for _ in range(numroll)]