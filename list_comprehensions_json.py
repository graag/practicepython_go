import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', required=True, help='plik json z lista liczb, ktorych beda wybrane parzyste (wymagany)')
args = parser.parse_args()

try:
    with open(args.file, 'r') as file:
            data = json.load(file)

    b = [elem for elem in data if elem%2 == 0]
    print(*b)
except(TypeError, ValueError):
    print("Nieprawidlowe warotsci w liscie")
except(FileNotFoundError):
    print("Nie znaleziono pliku")