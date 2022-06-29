from parent import Parent

class Child(Parent):
    def __init__(self, c1, **kwargs) -> None:
        super(Child, self).__init__(**kwargs)
        self.c1 = c1
        self.c2 = "c2"


chd1 = Child(p1="p1", p2="p2", c1="c1")
print(chd1.p1, chd1.p2, chd1.c1, chd1.c2)