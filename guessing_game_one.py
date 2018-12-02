import random

def game():
    num = random.randrange(1, 101)

    while True:
        while True:
            try:
                inp = int(input("Podaj liczbe od 1 do 100 ('0', zeby zakonczyc): "))
                break
            except(ValueError):
                print("Nieprawidlowo podana liczba")

        if inp == 0:
            break
        else:
            inp = int(inp)

        if inp < 1 or inp > 100:
            print("Co chcesz zrobic?")
        elif inp == num:
            print("Zgadles!")
            break
        elif inp < num:
            print("Za malo")
        else:
            print("Za duzo")

while(True):
    game()

    if input("Nowa gra? ('t') ") != 't':
        break