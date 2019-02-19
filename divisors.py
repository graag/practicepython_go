# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

try:
    num = int(input("Podaj liczbe: "))
except(ValueError):
    print("Podaj LICZBE")
    quit()

divisors = []

if num >= 2:
    for i in range(2,num):
            if num%i == 0:
                    divisors.append(i)

if num <=-2:
        for i in range(2,-num):
            if num%i == 0:
                    divisors.append(-i)

print("Dzielniki {}: 1, ".format(num), end="")
if divisors:
    print(*divisors, sep=", ", end=", ")
print("{}".format(num))