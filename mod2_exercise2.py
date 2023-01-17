#Jake Speiser

uString = str(input('Enter a string: '))

for x in range (0, len(uString)):
    if str(uString[x:x+1]).islower():
        print(uString[x:x+1], end="")

for x in range (0, len(uString)):
    if str(uString[x:x+1]).isupper():
        print(uString[x:x+1], end="")