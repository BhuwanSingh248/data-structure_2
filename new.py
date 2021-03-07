def show(mat):
    for i in mat:
        print(i)
def isvalid(data, visited, x, y):
    if x >= X or y >= Y or x<0 or y < 0 or visited[x][y] or data[x][y] == 0:
        return False
    return True

def BFS(data,i, j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    from collections import deque
    q = deque()
    q.append((i,j))
    count = 0
    while q:
        count+=1
        a,b = q.popleft()
        for k in range(4):
            if isvalid(data, visited, a+dx[k], b+dy[k]):
                q.append((a+dx[k], b+dy[k]))
                count+=1
            else:
                return count

if __name__ == "__main__":
    data = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1]
    ]

    X,Y = len(data), len(data[0])
    visited = [[False]*Y for _ in range(X)]
    count = 1
    for i in range(X):
        for j in range(Y):
            if data[i][j] == 1:
                data[i][j] = BFS(data, i, j)
    show(data)