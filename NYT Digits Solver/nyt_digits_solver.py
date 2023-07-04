"""
Goal: Be able to take 6 numbers and a target number 
and combine 6 or less numbers with one of the four simple math 
operators to get the target number
"""

# get these through i/o later on
numbers = [11,14,17,23,24,25]
target  = 421

# clear the file
with open('winningmove.txt', 'w') as fd:
    fd.write('')

# will at most need to look through 4*6! ==> 2880
class Node:
    def __init__(self, value, otherval, remaining, op='', parent=None):
        global target
        self.value = value
        self.otherval = otherval
        self.remaining = remaining
        self.op = op
        self.parent = parent

        if self.value == target:
            self.savewin()

        # children
        if len(self.remaining) > 0:
            self.adds = self.calc(self.add)
            self.subs = self.calc(self.sub)
            self.muls = self.calc(self.mul)
            self.divs = self.calc(self.div)

    def getop(self):
        return self.op

    def getvalue(self):
        return self.value
    
    def getother(self):
        return self.otherval

    def getparent(self):
        return self.parent

    def getstrop(self):
        if self.getop() == 'add':
            return '+'
        elif self.getop() == 'sub':
            return '-'
        elif self.getop() == 'mul':
            return 'x'
        elif self.getop() == 'div':
            return '/'

    def savewin(self):
        nodes = [] #op/parent pairs
        node = self
        while node != None:
            nodes.append(node)
            node = node.getparent()
            if node == None:
                break
        # could combine these if I wanted
        with open("winningmove.txt", 'a') as fd:
            for node in nodes:
                if node.getparent() != None :
                    fd.write(f'{node.getparent().getvalue()} {node.getstrop()} {node.getother()} = {node.getvalue()}\n')
            fd.write(f'\n')

    def valid(self, value):
        # no negatives
        if value < 0:
            return False
        # no fractions
        if (value - int(value)) > 0:
            return False
        return True
    
    def calc(self, op):
        output = []
        for ind,num in enumerate(self.remaining):
            value = op(self.value, num)
            if not self.valid(value):
                continue
            newremaining = self.remaining[0:ind] + self.remaining[ind+1:]
            node = Node(value, num, newremaining, op=op.__name__, parent=self)
            output.append(node)
        return output

    def add(self, a, b):
        return a+b
    
    def sub(self, a, b):
        return a-b
    
    def mul(self, a, b):
        return a*b
    
    def div(self, a, b):
        return a/b

# it seems to work if you just give it one starting number, no need to do all of them unless you want every single answer
# plus, it always seems to use every number. It would be challenging to optimize it to use as few as possible :)
roots = []
print("Solving...")
for ind,value in enumerate(numbers):
    remaining = numbers[0:ind] + numbers[ind+1:]
    newnode = Node(value, 0, remaining)
    roots.append(newnode)
print("Done")
# now I need to search through the nodes ...
# solved by checking at initialization