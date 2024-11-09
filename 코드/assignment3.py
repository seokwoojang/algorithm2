import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    answer = []
    binaryNode = sorted(nodeinfo, key= lambda x : (-x[1], x[0]))

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    
    root = Node(binaryNode[0])
    
    def insert(root, value):
        current_node = root
        while True:
            if value[0] < current_node.value[0]:
                if current_node.left == None:
                    current_node.left = Node(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right == None:
                    current_node.right = Node(value)
                    break
                else:
                    current_node = current_node.right
    
    for i in range(1, len(binaryNode)):
        insert(root, binaryNode[i])
    
    preorderList = []
    def preorder(root):
        if root != None:
            preorderList.append(nodeinfo.index(root.value) + 1)
            preorder(root.left)
            preorder(root.right)
    
    postorderList = []
    def postorder(root):
        if root != None:
            postorder(root.left)
            postorder(root.right)
            postorderList.append(nodeinfo.index(root.value) + 1)
    preorder(root)
    postorder(root)

    answer.append(preorderList)
    answer.append(postorderList)
    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
# result [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

print(solution(nodeinfo))