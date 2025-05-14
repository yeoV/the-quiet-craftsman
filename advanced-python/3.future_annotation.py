"""
future annotation
- class 객체처럼 이전에 명시된 것들을 references 할 수 있는, forward references!
- 사실 annotation은 str으로 표현한 후, Lazy Evaluation을 통해 실제 타입을 결정하는 것!
"""

from __future__ import annotations

class Node:
    def create(self) -> Node:   # Node가 내부적으로 문자열 처럼 저장되어 평가를 미루기 때문에 오류나지 않음.!
        return Node()


# PEP 563 에서 문제가 생김. pydantic 처럼 타입 정보를 바로 사용하는 경우가 많아짐..! 
# PEP 649 에서는 별도의 평가함수를 따로 만들어서 필요할 때 호출하도록 변경함!
# 솔직히 모르겠음
class function:
    # __annotations__ on a function object is already a
    # "data descriptor" in Python, we're just changing
    # what it does
    @property
    def __annotations__(self):
        return self.__annotate__()

def annotate_foo():
    return {'x': int, 'y': MyType, 'return': float}

def foo(x = 3, y = "abc"):
    ...

foo.__annotate__ = annotate_foo


# 3.11 ~ Self 타입쓰기. 오호 ?
from typing import Self

class Foo:
    def bar(self) -> Self:
        return self