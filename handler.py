import random
from smiles import smiles

def handle_message(dir, name):
    if name in smiles:
        return random.choice(dir[name])
    elif name == "Show me Stats":
    else:
        return "Smile is not found"


if __name__ == "__main__":
    print("Smile list: " + str(smiles.keys()))
    while True:
        smile_name = input("Your Message: ")
        ans = handle_message(smiles, smile_name)
        print(ans)

