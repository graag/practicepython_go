import random
max_length = 20
elem_range = 5 #do generowania list

def generate(length):
    l = []
    for i in range(1, length):
        l.append(random.randrange(elem_range))
    return l

def remove_duplicates(l):
    l.sort()

    for i in range(len(l) - 1, 0, -1):
        if l[i] == l[i - 1]:
            del l[i]
    return l
        

l = generate(random.randrange(1, max_length))

print("lista: ", end = "")
print(*l, sep = ", ")

remove_duplicates(l)

print("bez duplikatow: ", end = "")
print(*l, sep = ", ")

