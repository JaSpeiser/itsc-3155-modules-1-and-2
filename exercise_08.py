#Jake Speiser

list = []

for i in range(1,11):
    list.append(int(input('Enter number ' + str(i) + ': ')))

print('Original List: ' + str(list))

list2 = [x for x in list if list.count(x) == 1]

print('Nums that appear once: ' + str(list2))