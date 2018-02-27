import sys
import queue

class Node:
    def __init__(self, data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, root):
    # Write your code here
        nodes_to_search = queue.Queue()
        nodes_to_search.put(root)
        nodes_searched = ''
        while not nodes_to_search.empty():
            node = nodes_to_search.get()
            if node.left:
                nodes_to_search.put(node.left)
            if node.right:
                nodes_to_search.put(node.right)
            nodes_searched += str(node.data) + ' '
        print(nodes_searched)



T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)