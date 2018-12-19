class set:
    def __init__(self, values=None):
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        return "set: "+str(self.dict.keys())

    def add(self,value):
        self.dict[value] = True

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]


s = set([1, 2, 3, 4])
s.add(5)
print(s)
s.remove(2)
print(s)