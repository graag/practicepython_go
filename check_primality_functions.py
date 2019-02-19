#def divisors(num):
#    div = [elem for elem in range(2,num) if num%elem == 0]
#    return div 
def prim(num):
    for elem in range(2,num//2):
        if num%elem == 0:
            return False
    return True

def check_primality(num):
    if num < 2:
        print("{} to nie liczba pierwsza".format(num))
    elif prim(num):
        print("{} to liczba pierwsza".format(num))
    else:
        print("{} to nie liczba pierwsza".format(num))

try:
    check_primality(int(input("Podaj liczbe: ")))
except(ValueError):
    print("Wartosc nie jest liczba")
