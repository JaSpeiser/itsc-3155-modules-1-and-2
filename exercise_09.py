#Jake Speiser

list = []

for x in range(0,5):
    list.append(str(input("Enter a word: ")))

print('Words: ' + str(list))

print('One String:', end=" ")
for x in range(len(list)):
    print(list[x], end=" ")