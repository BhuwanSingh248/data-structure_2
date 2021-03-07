from collections import deque

r = [-1, -1, -1, 0, 1, 0, 1, 1]
c = [-1, 1, 0, -1, -1, 1, 0, 1]


def checkPreCondition(mat, processed, x, y):
    return (x>=0) and (x < len(processed)) and (y>=0) and (y < len(processed[0])) and (mat[x][y] == 1 and not processed[x][y])

def BFS(mat, processed, i, j):
    q = deque()
    q.append((i, j))

    processed[i][j] = True
    while q:
        x,y = q.popleft()
        for k in range(8):
            if checkPreCondition(mat, processed, x+r[k], y+c[k]):
                processed[x+r[k]] [y+c[k]] = True
                q.append((x+r[k], y+c[k]))



if __name__ == "__main__":
    mat = [
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
    ]

    R = len(mat)
    C = len(mat[0])
    processed = [[False]*C for _ in range(R)]

    island = 0
    for i in range(R):
        for j in range(C):
            if mat[i][j] == 1 and not processed[i][j]:
                BFS(mat, processed, i, j)
                island = island + 1
    
    print(island)





