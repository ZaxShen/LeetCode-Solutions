from random import choice

class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        l, d = self.l, self.d
        if val in d:
            idx, last_item = d[val], l[-1]
            l[idx], d[last_item] = last_item, idx
            l.pop()
            del d[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.l) 
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()