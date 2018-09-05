#encoding==utf-8

#Define the node of the binary tree
class Node:
    def __init__(self,data):
        self.data=data
        self.Lchild=None
        self.Rchild=None

#Define a binary tree structure
class Tree:
    def __init__(self):
        self.root=None  #Define the root node of the binary tree

    def add_child(self,data):  #Defines a function to add nodes
        node=Node(data)
        if self.root is None:
            self.root=node
        else:
            stk=[self.root]
            while True:
                temp_node=stk.pop(0)
                if temp_node.Lchild is None:
                    temp_node.Lchild=node
                    return
                elif temp_node.Rchild is None:
                    temp_node.Rchild=node
                    return
                else:
                    stk.append(temp_node.Lchild)
                    stk.append(temp_node.Rchild)



    def traverse(self):#Traverse a binary tree
        if self.root is None:
            return None
        stk=[self.root]
        res=[self.root.data]
        while stk!=[]:
            temp_node=stk.pop(0)
            if temp_node.Lchild is not None:
                stk.append(temp_node.Lchild)
                res.append(temp_node.Lchild.data)

            if temp_node.Rchild is not None:
                stk.append(temp_node.Rchild)
                res.append(temp_node.Rchild.data)
        return res

    def preorder(self,root):#The preorder traverses a binary tree
        if root is None:
            return []
        res=[root.data]
        Lchild_data=self.preorder(root.Lchild)
        Rchild_data=self.preorder(root.Rchild)
        return res+Lchild_data+Rchild_data

    def inorder(self,root):  #The inorder traverses a binary tree
        if root is None:
            return []
        res=[root.data]
        Lchild_data = self.inorder(root.Lchild)
        Rchild_data = self.inorder(root.Rchild)
        return Lchild_data+res+Rchild_data

    def postorder(self,root):  #The postorder traverses a binary tree
        if root is None:
            return []
        res=[root.data]
        Lchild_data = self.postorder(root.Lchild)
        Rchild_data = self.postorder(root.Rchild)
        return Lchild_data+ Rchild_data+res


tree=Tree()  #Initialize a binary tree
for i in range(10):  #Assign a value to a binary tree
    tree.add_child(i)
print(tree.traverse()) #Output the results of the traversal
print(tree.preorder(tree.root))#Output the result of preorder traversal
print(tree.inorder(tree.root))#Output the result of inorder traversal
print(tree.postorder(tree.root))#Output the result of postorder traversal
