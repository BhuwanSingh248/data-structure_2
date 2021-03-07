
def printmat(mat):
    for i in mat:
        print(i)

def isValid(mat, visted, x , y):
    if x<0 or y<0 or x >= X or y >= Y or visited[x][y] :
        return False
    if mat[x][y] == 1:
        return False
    return True

def BFS(mat, visited, i, j):
    # track = []
    dx = [1, -1, 0, 0]
    dy = [0 , 0, 1, -1]  
    from collections import deque
    q = deque()
    q.append((i, j))
    # track.append((i,j))
    mat[i][j] = "#"
    visited[i][j] = True

    while q:
        x, y  = q.popleft()
        for a,b in zip(dx, dy):
            if isValid(mat, visited, x+a, y+b):
                visited[x+a][y+b] = True
                q.append((x+a, y+b))
                mat[x+a][y+b] = "#"
    # return track           


if __name__ == "__main__":
    mat = [
        [1, 1, 1, 1, 1, 0],
        [1, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 1],
        [0, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1]
    ]

    X, Y = len(mat), len(mat[0])

    print(X, Y)
    visited = [[False] * Y for _ in range(X)]
    
    for i in range(X):
        for j in range(Y):
            if mat[i][j] == 0 and not visited[i][j] and (i==0 or j==0 or i==X-1 or j==Y-1):
               BFS(mat, visited , i, j)
    printmat(mat)
    for i in range(X):
        for j in range(Y):
            if mat[i][j] == 0:
                mat[i][j] = 1
            elif mat[i][j] == "#":
                mat[i][j] = 0
    printmat(mat)
