#Jake Speiser

list = []
maxSize = int(input('Enter a number: '))

for i in range(0, maxSize):
    elem = float(input('Enter a number ' + str(i) + ": "))
    list.append(elem)

print('List: ' + str(list))

listSum = 0

for x in list:
    listSum = listSum + x

print(listSum/maxSize)