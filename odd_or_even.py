while True:
        try:
                num = int(input("Podaj liczbe: "))
                check = int(input("Podaj dzielnik: "))
                if check == 0:
                        raise ValueError
                break
        except(ValueError):
                print("Nieprawidlowe wartosci")

if num%4 == 0:
        print("Liczba podzielna przez 4")
elif num%2 == 0:
        print("Liczba parzysta niepodzielna przez 4")
else:
        print("Liczba nieparzysta")


if num%check == 0:
        print("Liczba podzielna przez {}".format(check))
else:
        print("Liczba niepodzielna przez {}".format(check))