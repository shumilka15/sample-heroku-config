import random
from smiles import smiles
from smiles import stats


def handle_message(name):
    if name == "Stats":
        stats_p = [(i, stats[i]) for i in stats]
        return sorted(stats_p, key=lambda x: -x[1])
    elif name in smiles:
        stats[name] += 1
        return random.choice(smiles[name])
    else:
        return "Smile is not found"


if __name__ == "__main__":
    print("Smile list: " + str(smiles.keys()))
    while True:
        smile_name = input("Type 'Stats' if you want to see statistics.\nIf you want smiles type emotion!\nYour Message:")
        ans = handle_message(smile_name)
        print(ans)
