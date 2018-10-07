import random
max_length = 10
elem_range = 100 #do generowania list

def ends(l):
    e = [l[0], l[-1]]
    return e


def generate(length):
    l = []
    for i in range(1, length):
        l.append(random.randrange(elem_range))
    return l

l = generate(random.randrange(1, max_length))
print("lista: ", end = "")
print(*l, sep = ", ")
e = ends(l)
print("pierwszy element: {}, ostatni element: {}".format(e[0], e[1]))