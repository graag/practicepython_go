moves = {"kamien": 0, "papier": 1, "nozyce": 2}

def game(play1, play2):
    if play1 not in moves or play2 not in moves:
        print("Spojrz na tytul gry")
        return
    if (moves[play1] + 1)%3 == moves[play2]:
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

