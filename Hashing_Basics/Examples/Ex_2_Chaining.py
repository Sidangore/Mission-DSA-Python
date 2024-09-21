class MyHash:
    def __init__(self, b):
        self.bucket = b
        self.table = [[] for _ in range(b)]

    def insert(self, x):
        i = x % self.bucket
        self.table[i].append(x)

    def remove(self, x):
        i = x % self.bucket
        if x in self.table[i]:
            self.table[i].remove(x)

    def search(self, x):
        i = x % self.bucket
        return x in self.table[i]


if __name__ == '__main__':
    h = MyHash(7)
    h.insert(70)
    h.insert(10)
    h.insert(9)
    h.insert(56)
    print(h.search(11))
    print(h.search(10))
    h.remove(11)
    h.remove(10)
    print(h.search(10))
