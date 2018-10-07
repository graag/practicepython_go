def reverse(s):
    spl = s.split()
    result = " ".join([spl[-1-i] for i in range(len(spl))]) 
    return result

statement = input("Wpisz zdanie do odwrocenia: ")
print(reverse(statement))