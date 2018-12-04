import random
import argparse
import sys
import json

parser = argparse.ArgumentParser(description="Remove duplicates from a list")

def generate(length, ran):
    l = []
    try:
        for i in range(1, length):
            l.append(random.randrange(ran))
        return l
    except(ValueError):
        print("Invalid range")
        quit()

def remove_duplicates(l):
    return list(set(l))

if len(sys.argv) == 3:
    parser.add_argument('-m', type=int, help='-m=[max_length]')
    parser.add_argument('-r', type=int, help='-r=[elements_range]')
    args = parser.parse_args()

    try:
        length = random.randrange(1, args.m)
    except(ValueError):
        print("Invalid max length")
        quit()

    l = generate(length, args.r)
    print("list: ", end = "")
    print(*l, sep = ", ")

else:
    parser.add_argument('-f', type=str, help='-f=[filename.json]')
    args = parser.parse_args()

    try:
        with open(args.f, 'r') as file:
                data = json.load(file)

        l = data["a"]

    except(TypeError, ValueError):
        print("Nieprawidlowa lista")
        quit()

r = remove_duplicates(l)

print("without duplicates: ", end = "")
print(*r, sep = ", ")

