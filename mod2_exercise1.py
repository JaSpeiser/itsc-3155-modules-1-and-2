#Jake Speiser

uString = str(input('Enter a string: '))
strSize = len(uString)

while strSize >= 0:
    print(uString[strSize:strSize+1],end="")
    strSize = strSize - 1