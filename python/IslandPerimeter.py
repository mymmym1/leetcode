def islandPerimeter(grid):
    outerland = 0
    inland = 0
    halfland = 0
    oneside = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1: 
                count = 0
                if j-1>=0 and grid[i][j-1]==1:
                    count += 1
                if j+1<len(grid[i]) and grid[i][j+1]==1:
                    count += 1
                if i-1>=0 and grid[i-1][j]==1:
                    count += 1
                if i+1<len(grid) and grid[i+1][j] == 1:
                    count += 1

                if count == 4:
                    inland += 1
                if count == 2:
                    halfland += 1
                if count == 3:
                    oneside += 1
                if count == 1:
                    outerland += 1
                if count == 0:
                    return(4)

    perimeter = outerland*3 + halfland*2 + oneside
    return perimeter

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
grid = [[1]]
grid = [[1,0]]
print(islandPerimeter(grid))
