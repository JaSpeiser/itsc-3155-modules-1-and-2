#Jake Speiser

characters = list(input('Enter a string: '))

split_list = []
for i in range(0, len(characters), 3):
    split_list.append(characters[i:i+3])

print(split_list)
