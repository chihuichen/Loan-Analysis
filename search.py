class Node():
    def __init__(self, key):
        self.key = key
        self.values = []
        self.left = None
        self.right = None
        
    def __len__(self):
        size = len(self.values)
        if self.left != None:
            size += len(self.left.values)
        if self.right != None:
            size += len(self.right.values)
        return size
    
    def lookup(self, target):
        if target == self.key:
            return self.values
        if self.left != None:
            if target < self.key:
                return self.left.lookup(target) 
        if self.right != None:
            if target > self.key:
                return self.right.lookup(target)
        else:
            return []
        
    def height(self):
        if self.left == None:
            l = 0
        else:
                # recurse left
            l = self.left.height()

        if self.right == None:
            r = 0
        else:
                # recurse right
            r = self.right.height()

        return max(l, r)+1



class BST():
    def __init__(self):
        self.root = None

    def add(self, key, val):
        if self.root == None:
            self.root = Node(key)
        curr = self.root
        while True:
            if key < curr.key:
                # go left
                if curr.left == None:
                    curr.left = Node(key)
                curr = curr.left
            elif key > curr.key:
                 # go right
                if curr.right == None:
                    curr.right = Node(key)
                curr = curr.right
            else:
                # found it!
                assert curr.key == key
                break
        curr.values.append(val)
        
    def __dump(self, node):
        if node == None:
            return 
        print(node.key, ":", node.values)
        self.__dump(node.right) 
        self.__dump(node.left)             

    def dump(self):
        self.__dump(self.root)
    
    def __getitem__(self, key):
        return self.root.lookup(key)
    
    def height(self):
        return self.root.height()
    
    def getLeafCount(self):
        return self.root.getLeafCount()
    


   

t = BST()
t.add("B", 3)
assert len(t.root) == 1
t.add("A", 2)
assert len(t.root) == 2
t.add("C", 1)
assert len(t.root) == 3
t.add("C", 4)
assert len(t.root) == 4
        