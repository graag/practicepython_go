def reverse(s):
    spl = s.split()
    result = " ".join(spl[::-1]) 
    return result

statement = input("Wpisz zdanie do odwrocenia: ")
print(reverse(statement))