class MyHash:
    def __int__(self, cap):
        self.cap = cap
        self.table = [-1 for _ in range(cap)]
        self.size = 0

    def hash(self, x):
        return x % self.cap

    def search(self, x):
        h = self.hash(x)
        t = self.table
        i = h
        while t[i] != -1:
            if t[i] == x:
                return True
            i = (i + 1) % self.cap
            if i == h:
                return False
        return False

    def insert(self, x):
        if self.size == self.cap:
            return False
        if self.search(x):
            return False
        i = self.hash(x)
        t = self.table
        while t[i] not in (-1, -2):
            i = (i + 1) % self.cap
        t[i] = x
        self.size += 1
        return True

    def remove(self, x):
        if self.size == 0:
            return False
        h = self.hash(x)
        t = self.table
        i = h
        while t[i] != -1:
            if t[i] == x:
                t[i] = -2
                self.size -= 1
                return True
            i = (i + 1) % self.cap
            if i == h:
                return False
        return False
