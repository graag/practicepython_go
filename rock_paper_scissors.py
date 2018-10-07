dict = {"kamien": 0, "papier": 1, "nozyce": 2}

def game(play1, play2):
    if play1 not in dict or play2 not in dict:
        print("Spojrz na tytul gry")
        return
    if (dict.get(play1) + 1)%3 == dict.get(play2):
        print("Wygral gracz 2")
    elif play1 == play2:
        print("Remis")
    else:
        print("Wygral gracz 1")

while(True):
    pl1 = input("Ruch gracza 1: ")
    pl2 = input("Ruch gracza 2: ")
    game(pl1, pl2)
    if input("Nowa gra? ('t') ") != 't':
        break

