
def explore_neighbours(row, col):
    global R, C, visited, grid,xq,yq,node_in_next_layer
    for i in range(4):
        rr = row + dr[i]
        cc = col + dc[i]
        if rr < 0 or cc < 0 or rr >= R or cc >= C or visited[rr][cc]: continue
        else:print(grid[rr][cc])
        xq.append(rr)
        yq.append(cc)
        visited[rr][cc] = True
        node_in_next_layer+=1


def solve():
    global xq, yq, sr, sc, visited
    xq.append(sr)
    yq.append(sc)

    visited[sr][sc] = True
    while len(xq) > 0:
        r = xq.pop(0)
        c = yq.pop(0)   
        explore_neighbours(r, c)

if __name__ == "__main__":
    grid = [[(i, j) for j in range(10)] for i in range(10)]
    R = len(grid)
    C = len(grid[1])
    visited = [[False] * R for _ in range(C)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    node_left_in_layer = 1
    node_in_next_layer = 0
    reached_end = False
    sr,sc = 0, 0
    xq, yq = [],[]
    solve()
    print(visited)
