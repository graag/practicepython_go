import sys

word = input("Podaj slowo: ")
for i in range(len(word)//2):
    if word[i] != word[-i-1]:
        print("Nie palindrom")
        sys.exit(0)
print("Palindrom")