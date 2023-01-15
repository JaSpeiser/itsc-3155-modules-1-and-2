#Jake Speiser

list1 = []
list2 = []
list3 = []

for i in range(0, 5):
    elem = int(input('Enter a number for the first list: '))
    list1.append(elem)

for i in range(0, 5):
    elem = int(input('Enter a number for the second list: '))
    list2.append(elem)

print(str(list1))
print(str(list2))

for i in range(0,5):
    if list1[i] in list2:
        list3.append(list1[i])

print(str(list3))