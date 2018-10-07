import random
max_length = 20
elem_range = 10 #do generowania list

def generate(length):
    l = []
    for i in range(1, length):
        l.append(random.randrange(elem_range))
    return l

def remove_duplicates(l):
    return list(set(l))

l = generate(random.randrange(1, max_length))
r = remove_duplicates(l)

print("lista: ", end = "")
print(*l, sep = ", ")
print("bez duplikatow: ", end = "")
print(*r, sep = ", ")

