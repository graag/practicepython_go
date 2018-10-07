num = int(input("Podaj liczbe: "))
check = int(input("Podaj dzielnik: "))
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