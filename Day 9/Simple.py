class Tree:

    def __init__(self, name, branch, leaves):
        self.name = name
        self.branch = branch
        self.leaves = leaves
    
    def getTree(self):
        print(self.name + " tree and has branch of " + str(self.branch) + " with leaves "+ str(self.leaves))

class Fruits(Tree):

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
        super().__init__(name, branch, leaves= 3)

    def getName(self):
        print(self.name)

class Apple(Fruits):

    def __init__(self, name, branch):
        super().__init__(name, branch)

# extenal object
apple = Apple(name="apple", branch=1)

apple.getTree()
apple.getName()


    

