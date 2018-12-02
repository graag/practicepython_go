import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('jsonfile')
args = parser.parse_args()

try:
    with open(args.jsonfile, 'r') as file:
            data = json.load(file)

    a = data["a"]

    b = [elem for elem in a if elem%2 == 0]
    print(*b)
except(TypeError, ValueError):
    print("Nieprawidlowe warotsci w liscie")