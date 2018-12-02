a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []

while True:
    try:
        num = int(input("Podaj liczbe: "))
        break
    except(ValueError):
        pass

b = [element for element in a if element < 5]
c = [element for element in a if element < num]

print("Mniejsze, niz 5: ", end = "")
print(*b, sep = ", ")

print("Mniejsze, niz {}: ".format(num), end ="")
print(*c, sep = ", ")