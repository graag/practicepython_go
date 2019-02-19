import random
max_length = 10
elem_range = 100 

def ends(l):
   # e = [l[0], l[-1]]
   # return e
   return l[0], l[-1]


def generate(length):
    l = []
    for i in range(1, length):
        l.append(random.randrange(elem_range))
    return l

#obie opcje losują próbkę ze zwracaniem
try:
    len = int(input("Rozmiar populacji do utworzenia listy (dla <=0 generuj w domyslny sposob): "))
    if len > 0:
        n = int(input("Rozmiar listy: "))
        l = random.choices(range(len), k=n)
    else:
        print("domyslna")
        l = generate(random.randrange(1, max_length))
except(ValueError, TypeError):
    print("Podawaj liczby calkowite")     
    quit()

print("lista: ", end = "")
print(*l, sep = ", ")
#e = ends(l)
start, end = ends(l)
print("pierwszy element: {}, ostatni element: {}".format(start, end))