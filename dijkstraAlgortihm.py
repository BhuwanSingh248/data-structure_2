def selectMinVertex(value, processed):

    minimum = maxsize
    for i in range(node):
        print(i)
        if not processed[i] and value[i] < minimum:
            vertex = i
            minimum = value[i]
    return vertex

def dijkstra(mat):
    parent = [-1]*node
    value = [maxsize]*node
    processed = [False]*node
    value[0] = 0

    for i in range(node-1):
        u = selectMinVertex(value, processed)
        processed[u] = True
        for j in range(node):
            if mat[u][j] !=0 and not processed[j] and value[u] != maxsize and value[u]+ mat[u][j]<value[j]:
                value[j] = value[u] + mat[u][i]
                parent[j] = u 
    return parent, value

if __name__ == "__main__":
    from sys import maxsize
    mat = [
        [0, 1, 4, 0, 0, 0],
		[1, 0, 4, 2, 7, 0],
		[4, 4, 0, 3, 5, 0],
		[0, 2, 3, 0, 4, 6],
		[0, 7, 5, 4, 0, 7],
        [0, 0, 0, 6, 7, 0],
    ]
    node = len(mat)
    print(dijkstra(mat))
