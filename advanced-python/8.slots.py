# classes 의 attributes 를 고정하고 속도 증진
# 하지만 효과가 미미해서 그닥 .. 굳이...

class FooBar:
    __slots__ = ("a", "b", "c")
    
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

f = FooBar()
print(f.__slots__)