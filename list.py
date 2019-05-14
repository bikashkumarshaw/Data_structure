class List(object):
    def __init__(self, init=None):
        self.value = init
        self.next = None

    def append(self, value):
        if not self.value:
            self.value = value
        elif self.next is not None:
            self.next.append(value)
        else:
            self.next = List(value)

    def insert(self, value, pos=0):
        temp = self
        count = 0
        while(count<pos):
            temp = temp.next
            count = count+1
        if not temp.value:
            temp.value = value
        new_node = List(temp.value)
        new_node.next = temp.next
        temp.value = value
        temp.next = new_node

    def delete(self, value):
        if not self.value:
            return ()
        if self.value == value:
            self.value = self.next.value
            self.next = self.next.next
            return ()
        temp = self
        while(temp.next.next!=None):
            if temp.value==value:
                temp.value = temp.next.value
                temp.next = temp.next.next
                return ()
            else:
                temp = temp.next
        temp.next = None

    def pop(self, pos=-1):
        tmp = self
        if pos<0:
            while(tmp.next.next!=None):
                tmp = tmp.next
            tmp.next = None
        else:
            count = 0
            while(count<pos):
                tmp = tmp.next
                count = count+1
            tmp.value = tmp.next.value
            tmp.next = tmp.next.next

    def __str__(self):
        lis = []
        temp = self
        while(temp.next!=None):
            lis.append(temp.value)
            temp = temp.next
        lis.append(temp.value)
        return str(lis)

    def PrintTree(self):
        if self.next:
            print self.value
            self.next.PrintTree()
        else:
            print self.value
