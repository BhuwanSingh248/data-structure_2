map = {1:(2,7), 2:(1,5), 3:(7,), 4:(6,), 5:(2,6), 6:(5,7), 7:(6,2,1)}
visited = [{i:False} for i in map.keys()]
from collections import deque
stack = deque()

print(visited)
