import random
import sys

ascii_min = 33
ascii_max = 126
min_length = 10
max_length = 15 
lines_in_file = 124
weak_min_length = 5

def strong_password(r):
    length = r.randint(min_length, max_length)
    password = []
    for i in range(length):
        password.append(chr(r.randint(ascii_min, ascii_max)))
    password = "".join(password)
    return password

def weak_password(r):
    i = 0
    with open("weak_password", "r") as file:
        rand_line_num = r.randint(1, lines_in_file)
        line = file.readline()
        word = ""
        i = 1
        while line:
            if i == rand_line_num:
                word_list = line.split()
                word = word_list[r.randint(0, len(word_list) - 1)]
                if len(word) > 5:
                    return word
                    break
            else:
                line = file.readline()
                i = i + 1

rand = random.SystemRandom()
while (True):
    inp = (input("w - generuj slabe haslo, s - generuj silne haslo, dowolne - wyjdz: "))
    if (inp == 's'):
        print(strong_password(rand))
    elif(inp == 'w'):
        print(weak_password(rand))
    else:
        break

