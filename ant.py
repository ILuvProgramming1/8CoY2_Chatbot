
grid = []
width = 10
height = width

def printGrid(grid):
    for row in grid:
        for col in row:
            print(f" {col} ", end='')
        print()

for row in range(height):
    grid.append([])
    for col in range(width):
        grid[-1].append(0)

ant = [width//2, height//2]
direction = 0 # 0: north, 1: east, 2: south, 3: west

while True:
    printGrid(grid)
    if grid[ant[1]][ant[0]] == 0: # black pixel
        grid[ant[1]][ant[0]] = 1
        direction -= 1
        if direction < 0:
            direction = 3
    elif grid[ant[1]][ant[0]] == 1: # black pixel
        grid[ant[1]][ant[0]] = 0
        direction += 1
        if direction > 3:
            direction = 0
    if direction == 0:
        ant[1] -= 1
    elif direction == 1:
        ant[0] += 1
    elif direction == 2:
        ant[1] += 1
    elif direction == 3:
        ant[0] -= 1
    input()


