import random

a = []
b = []
max_length = 10
min_length = 5

def generate(list, length):
        for i in range(1, length):
                list.append(random.randrange(10))

generate(a, random.randrange(min_length, max_length))
generate(b, random.randrange(min_length, max_length))

overlap = set([element for element in a if element in b])

print("a = ", end = "")
print(*a, sep = ", ")
print("b = ", end = "")
print(*b, sep = ", ")
print("overlap = ", end = "")
print(*overlap, sep = ", ")