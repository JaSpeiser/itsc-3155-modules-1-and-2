#Jake Speiser

grid = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

row = int(input('Enter a row num from 1 to 5: '))
col = int(input('Enter a col num from 1 to 5: '))

grid[row-1][col-1] = 1

for x in grid:
    for i in x:
        print(i,end=" ")
    print()