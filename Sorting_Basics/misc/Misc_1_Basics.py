class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __lt__(self, other):
    #     return self.age < other.age

    def __gt__(self, other):
        return self.name > other.name


members = [Member("siddhant", 24),
           Member("niharika", 17),
           Member("vibha", 48),
           Member("jayant", 52)]

sorted_mem = sorted(members)

for m in sorted_mem:
    print(m.name, m.age)

