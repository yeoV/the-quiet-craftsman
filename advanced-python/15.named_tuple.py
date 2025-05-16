from dataclasses import dataclass, field
from typing import NamedTuple


# -------- NamedTuple --------
class Result(NamedTuple):
    ok : bool
    data : str | None = None
    items: list = []


# __new__ 로 데이터 객체를 생섣!
# res = Result(ok=False) # Result.__new__() missing 1 required positional argument: 'data' 
res = Result(ok=False, data=None)
print(dir(res))
"""
! 사실상 __dict__ 는 존재하지 않음. -> Tuple 타입을 받은 것 이기 떄문.!
['__add__', '__annotations__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__match_args__', '__module__', '__mul__', '__ne__', '__new__', '__orig_bases__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '_asdict', '_field_defaults', '_fields', '_make', '_replace', 'count', 'data', 'index', 'ok']
"""


# NamedTuple 타입은 import 되어 사용될 때, 가변 변수를 생성해서 속성값에 넣기 때문에 값을 서로 공유함.!(tuple 타입이니까..?)
a = Result(ok=False)
b = Result(ok=False)
a.items.append("Hello world!")
print(b.items)  # 'Hello world!']

"""
# https://github.com/python/cpython/blob/main/Lib/collections/__init__.py 421 line
# deep dive

사실상 NamedTuple 은 
collections.namedtuple 의 구현체.!

defaults = tuple(defaults)
    if defaults is not None:
        __new__.__defaults__ = defaults


이것처럼 클래스 생성 시점에 동적으로 __new__를 만들고, __new__.__defaults__ 속성에 Tuple(defaults) 를 딱 한번 넣음
그래서 mutable이기 떄문에 가변인자 공유가 나타나는 것임..        
"""


# # -------- dataclass --------
@dataclass
class DataResult():
    ok : bool
    data : str | None = None


c_a = DataResult(ok=True)
print(c_a.__dict__) # 기본 객체는 __dict__ 타입으로 속성을 저장함

# #slot 을 사용하여 메모리 사용량 감소 시키기.
@dataclass(frozen=True, slots=True)
class SlotResult():
    ok : bool
    data : str | None = None
    items : list = field(default_factory=list)

s_a = SlotResult(ok=True)
# print(s_a.__dict__) # AttributeError: 'SlotResult' object has no attribute '__dict__'. Did you mean: '__dir__'?

s_b = SlotResult(ok=True)
s_a.items.append("Hello world!")
print(s_b.items)    # default factory 는 서로 공유 안함

        
