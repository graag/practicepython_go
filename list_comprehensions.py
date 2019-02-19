a = [i**2 for i in range(10)]
b = [elem for elem in a if elem%2 == 0]
print(*b)