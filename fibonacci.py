def fibonacci(num):
    seq = [1, 1]
    if num < 1:
        return []
    elif num == 1:
        return seq[:-1]
    elif num == 2:
        pass
    else:
        for i in range(2, num):
            seq.append(seq[i - 1] + seq[i - 2])
    return seq

try:
    len = int(input("Podaj dlugosc sekwencji: "))
    
    if(len > 0):
        f = fibonacci(len)
        print(*f, sep = ", ")
    else:
        raise ValueError

except(ValueError):
    print("Nieprawidlowo podana dlugosc")
