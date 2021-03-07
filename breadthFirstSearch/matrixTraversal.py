a = [[(i,j) for i in range(5)] for j in range(5)]
dr = [-1, 1, 0, 0] 
dc = [0, 0, 1, -1]
for _ in a:
    print(_)
r = 1
c = 1
R = len(a)
C = len(a[0])
for i in range(len(dr)):
    rr = r + dr[i]
    cc = c + dc[i]
    if rr < 0 or cc < 0: continue
    if rr >= R or cc >= C: continue
    print(a[rr][cc])
    