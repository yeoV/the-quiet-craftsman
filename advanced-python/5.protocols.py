# Major typing 중 하나!
# Duck Typing 전용!  “If it walks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.”

class Duck:
    def quack(self): print("Quick!")

class Person:
    def quack(self): print("I'm a person, but I can quack like a duck!")

class Dog:
    def bark(self): print("Woof!")

def run_quack(obj):
    obj.quack()


run_quack(Duck())
run_quack(Person())
run_quack(Dog())    # Runtime에서 오류 발생

# Typechecking 단계에서 오류 잡기!
from typing import Protocol

class Quackable(Protocol):
    def quack(self) -> None: ...
    
class Duck2:
    def quack(self): print("Quick!")

class Dog2:
    def bark(self): print("Woof!")

def run_quack2(obj: Quackable):
    obj.quack()

run_quack2(Duck2())
# run_quack2(Dog2())   # Typechecking 단계에서 오류 발생

# Runtime 환경에서 isInstance로 비교하고 싶다면 데코레이터 추가
from typing import runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None: ...