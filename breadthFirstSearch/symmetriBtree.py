class newNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
def isSymmetric(root):
    if root == None:
        return True
    if not root.left and not root.right:
        return True
    
    q = []

    q.append(root)
    q.append(root)

    leftNode = 0
    rightNode = 0

    while not len(q):

        leftNode = q[0]
        q.pop(0)

        rightNode = q[0]
        q.pop(0)

        if leftNode.key != rightNode.key:
            return False
        
        if leftNode.left and rightNode.right :
            q.append(leftNode.left)
            q.append(rightNode.right)

        elif leftNode.left or rightNode.right :
            return False
        
        if leftNode.right and rightNode.left:
            q.append