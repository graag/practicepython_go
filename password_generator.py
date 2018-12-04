import random
import sys

ascii_min = 33
ascii_max = 126
min_length = 10
max_length = 15 
weak_min_length = 5

def strong_password(r):
    length = r.randint(min_length, max_length)
    password = []
    for i in range(length):
        password.append(chr(r.randint(ascii_min, ascii_max)))
    password = "".join(password)

    return password

def weak_password(r):
    with open("weak_password", "r") as file:     
        lines = file.readlines()

    rand_line_num = r.randint(0, len(lines) - 1)
    word = ""        
    word_list = lines[rand_line_num].split()
    word = word_list[r.randint(0, len(word_list) - 1)]             
    while(len(word) < weak_min_length):
        word = word + '1'

    return word

rand = random.SystemRandom()
while (True):
    inp = (input("w - generuj slabe haslo, s - generuj silne haslo, dowolne - wyjdz: "))
    if (inp == 's'):
        print(strong_password(rand))
    elif(inp == 'w'):
        print(weak_password(rand))
    else:
        break

