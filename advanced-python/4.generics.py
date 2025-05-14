

# ~3.11 까지 버전
from typing import TypeVar, Generic

Unbounded = TypeVar("Unbounded")
Bounded = TypeVar("Bounded", bound=int)
Constained = TypeVar("Constained", int, float)

class OldFoo(Generic[Unbounded, Bounded, Constained]):
    def __init__(self, x: Unbounded, y: Bounded, z: Constained) -> None:
        self.x = x
        self.y = y
        self.z = z
    


# 쓰읍 근데 변수 파악하기 너무 빡세지 않나? 이전 버전이 조금 명시적이지 않나?
class Foo[UnBounded, Bounded: int, Constained : int | float]:
    def __init__(self, x: UnBounded, y: Bounded, z: Constained) -> None:
        self.x = x
        self.y = y
        self.z = z


# Go 언어같은 Typevar
# ~3.11
from typing import TypeAlias
_Vector: TypeAlias = list[float]

# 3.12
# 요건 밑에가 더 편한듯
type Vector = list[float]
        

old_foo = OldFoo("hello", 1, 2.0)
print(old_foo.x)
print(old_foo.y)
print(old_foo.z)
foo = Foo("hello", 1, 2.0)
print(foo.x)
print(foo.y)
print(foo.z)
