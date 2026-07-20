class NestedIterator:

    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):

        while self.stack:

            top = self.stack[-1]

            if top.isInteger():
                return True

            self.stack.pop()

            lst = top.getList()

            for x in reversed(lst):
                self.stack.append(x)

        return False