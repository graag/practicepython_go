import random
import argparse
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

parser.add_argument('-f', '--file', type=str, help='json file containing a list of integers')
parser.add_argument('-m', '--max', type=int, help='max length of list of random integers')
parser.add_argument('-r', '--range', type=int, help="range of random integers' value")

args = parser.parse_args()

if args.file is not None:
    try:
        with open(args.file, 'r') as file:
            l = json.load(file)

    except(TypeError, ValueError):
        print("Invalid list")
        quit()
    except(FileNotFoundError):
        print("File not found")
        quit()
elif args.max is not None and args.range is not None:  
    try:
        length = random.randrange(1, args.max)
        l = generate(length, args.range)
        print("list: ", end = "")
        print(*l, sep = ", ")
    except(ValueError):
        print("Invalid max length or range")
        quit()
else:
    parser.print_help()
    quit()

r = remove_duplicates(l)

print("without duplicates: ", end = "")
print(*r, sep = ", ")

