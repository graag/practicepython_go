import random

def compare(spl1, spl2):
    cows = 0
    bulls = 0
    scored = [0] * 4

    for i in range(4):
        if spl1[i] == spl2[i]:
            cows = cows + 1
            scored[i] = 1

    for i in range(4):
        if spl2[i] in spl1 and scored[i] == 0:
            bulls = bulls + 1
            scored[i] = 1

    return [cows, bulls]

def game():
    num = str(random.randrange(1000, 10000)) 
    print(num)
    count = 0

    while(True):    
        while True:
            try:
                inp = int(input("Podaj czterocyfrowa liczbe (0, zeby zakonczyc): "))
                break
            except(ValueError):
                pass

        if inp == 0:
            break
        elif int(inp) < 1000 or int(inp) > 9999:
            print("Co chcesz zrobic?")
        else:
            result = compare(str(inp), str(num))
            count = count + 1
            print("{} cows, {} bulls".format(result[0], result[1]))
            if result[0] == 4:
                print("Zgadles! Liczba podejsc: {}".format(count))
                break
            

if __name__=="__main__":
    while(True):
        game()
        if input("Nowa gra? ('t') ") != 't':
            break