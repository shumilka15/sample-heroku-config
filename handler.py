smiles = {'Angry':"┌( ◕ 益 ◕ )ᓄ", 'Ugly':"(   ͡°╭╮ʖ   ͡°)", 'Upset':"( ຈ ﹏ ຈ )", 'Cool':"⊂(▀¯▀⊂)", 'Meh':"(╭ರ_⊙)"}

def handle_message(dir, name):
    if name in smiles:
        return dir[name]
    else:
        return "Smile is not found"


if  __name__ == "__main__":
    print("Smile list: " + str(smiles.keys()))
    while True:
        smile_name = input("Enter necessary smile name: ")
        ans = handle_message(smiles, smile_name)
        print(ans)
