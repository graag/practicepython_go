def divisors(num):
    div = [elem for elem in range(2,num) if num%elem == 0]
    return div 

def check_primality(num):
    if num < 2:
        print("{} to nie liczba pierwsza")
    elif not divisors(num):
        print("{} to liczba pierwsza")
    else:
        print("{} to nie liczba pierwsza")

check_primality(int(input("Podaj liczbe: ")))
