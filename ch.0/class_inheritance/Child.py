from Parent import Parent

class Child(Parent):
    def __init__(self, c1, **kwargs):
        super(Child, self).__init__(**kwargs)
        self.c1 = c1
        self.c2 = "C2"

child = Child(p1="p1", p2="p2", c1="c1")

print(child.p1)
print(child.p2)
print(child.c1)
print(child.c2)