class BST(object):
    def __init__(self, val=None):
        self.value = val
        self.left = None
        self.right = None

    def insert(self, val):
        if not self.value:
            self.value = val

        if self.value==val:
            return

        if val<self.value and self.left != None:
            self.left.insert(val)
        elif val<self.value and self.left == None:
            self.left = BST(val)

        if val>self.value and self.right != None:
            self.right.insert(val)
        elif val>self.value and self.right == None:
            self.right = BST(val)

    def search(self, val):
        if not self.value:
            return

        if self.value==val:
            return True

        if val<self.value and self.left !=None:
            Found = self.left.search(val)
            return Found

        if val>self.value and self.right != None:
            Found = self.right.search(val)
            return Found

        return False

    def delete(self, val):
        if not self.value:
            return

        if self.value == val:
            if self.left == None and self.right == None:
                self.value = None
                return
            elif self.left == None:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return
            elif self.right == None:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
                return
            else:
                tmp = self.left
                while(tmp.right!=None):
                    tmp = tmp.right
                self.value = tmp.value
                self.delete(tmp.value)

        if val<self.value and self.left!=None:
            self.left.delete(val)

        if val>self.value and self.right!=None:
            self.right.delete(val)

    def PrintTree(self):
        if self.left and self.left.value!=None:
            self.left.PrintTree()

        print self.value

        if self.right and self.right.value!=None:
            self.right.PrintTree()
