global R, C, rq, cq, sr, sc, reached_end, move_count, node_left_in_layer,node_in_next_layer, vidited, dr, dc

sr, sc  = 0 ,0  # row and column value 
rq, cq = [],[]  # row and column queue 

move_count = 0
node_left_in_layer = 1
node_in_next_layer = 0
reached_end = False
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]



def explore_neighbours(row, col):
    global R, C, rq, cq, sr, sc, reached_end, move_count, node_left_in_layer,node_in_next_layer, vidited, dr, dc

    for i in range(4):
        rr = row + dr[i]
        cc = col + dc[i]
        if rr < 0 or cc < 0: continue
        if rr >= R or cc >= C: continue
        if visited[rr][cc]:continue
        if problemMatrix[rr][cc] == '#':continue
        rq.append(rr)
        cq.append(cc)
        visited[rr][cc] = True
        node_in_next_layer += 1 
def solve():
    global R, C, rq, cq, sr, sc, reached_end, move_count, node_left_in_layer,node_in_next_layer, vidited, dr, dc
    rq.append(sr)
    cq.append(sc)
    visited[sr][sc] = True
    while len(rq) > 0:
        r = rq.pop(0)
        c = cq.pop(0)
        if problemMatrix[r][c] == "E":
            reached_end = True
            break
        explore_neighbours(r, c)
        node_left_in_layer -= 1
        if node_left_in_layer == 0:
            node_left_in_layer = node_in_next_layer
            node_in_next_layer = 0
            move_count += 1
    if reached_end:
        return move_count
    return -1

problemMatrix = [
    ['S', '_', '_', '#', '_', '_', '_'],
    ['_', '#', '_', '_', '_', '_', '_'],
    ['_', '#', '_', '_', '_', '_', '_'],
    ['_', '_', '#', '#', '_', '_', '_'],
    ['#', '_', '#', 'E', '_', '#', '_'],
    ]

R,C = len(problemMatrix), len(problemMatrix[0])
visited = [[(False) for i in range(C)] for j in range(R)]


print(solve())
