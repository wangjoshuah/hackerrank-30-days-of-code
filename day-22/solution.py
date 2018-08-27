class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data


class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self, root):
        if not root:
            return -1
        elif not root.left and not root.right:
            return 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        return max(left_height, right_height) + 1


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
