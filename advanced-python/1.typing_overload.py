"""
@overload 는 사실상 정적검사를 위한 데코레이터.
기존 함수를 구현해 두고, 정적검사에 도움을 주기 위해서 만드는 것.

overload가 없다면 정적검사에서 에러를 잡아내지 않음!
!! Runtime에 실행되지 않음.!!
"""

from typing import Literal, overload


@overload
def transform(data: str, mode: Literal["split"]) -> list[str]: ...
@overload
def transform(data: str, mode: Literal["upper"]) -> str: ...

def transform(data: str, mode: Literal["split", "upper"]):
    if mode == "split":
        return data.split()
    elif mode == "upper":
        return data.upper()


split_words = transform("hello", "split")
# split_words.upper() # error Overload가 없으면 정적 단계에서 에러를 잡아내지 않음..! 



