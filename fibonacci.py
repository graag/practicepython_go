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

f = fibonacci(int(input("Podaj dlugosc sekwencji: ")))
print(*f, sep = ", ")
