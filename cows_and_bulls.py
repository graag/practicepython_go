import random

def compare(spl1, spl2):
    cows = 0
    bulls = 0
    for i in range(4):
        if spl1[i] == spl2[i]:
            cows = cows + 1
        elif spl1[i] in spl2:
            bulls = bulls + 1
    return [cows, bulls]

def game():
    num = str(random.randrange(1000, 10000)) 
    print(num)
    count = 0

    while(True):    
        inp = input("Podaj czterocyfrowa liczbe ('x', zeby zakonczyc): ")  

        if inp == 'x':
            break
        elif not inp.isdigit() or int(inp) < 1000 or int(inp) > 10000:
            print("Co chcesz zrobic?")
        else:
            result = compare(inp, num)
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