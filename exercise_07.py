#Jake Speiser

list1 = []
list2 = []

while True:
    elem = input('Enter a number or QUIT to quit: ')

    if elem == 'QUIT':
        break
    else:
        list1.append(int(elem))

print('All nums: ' + str(list1))

for x in range(0,len(list1)):
    if list1[x] % 2 == 0:
        list2.append(list1[x])

print('Even nums: ' + str(list2))