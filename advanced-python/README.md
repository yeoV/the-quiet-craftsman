## Python Advanced Features 를 위한 것!
https://blog.edward-li.com/tech/advanced-python-features
- 맛있다!

#### 1. Typing Overloads
- 단순하게 정적검사를 위해 명시해 두는 것!
- Java의 오버라이딩과는 다른 개념
- [소스코드](1.typing_overload.py)

#### 2. Keyword-only and Positional-only Arguments
- 사실 언제써야할지 잘 모르겠음

#### 3. Future Annotations
- lazy evaluation을 통해 forward references를 가능하도록 하는 것!
- 하지만, pydantic, ORM 쓸때는 주의해야할지도?
- [소스코드](3.future_annotation.py)

#### 4. Generics
- Generics은 늘 편하다.
- 그치만 가독성 생각해서 변수명 잘 만들 자신있으면 시원하게?
- type 정의 기능은 go언어 같아서 좋다
- [소스코드](4.generics.py) 


#### 5. Protocols
- interface 나 상속없이 정의해야하는 structure나 behavior를 정의할 수 있는 Duck Typing!
- [소스코드](5.protocols.py)


#### 6. Context Managers
#### 7. Structural Pattern Matching
#### 8. Python Slots
- __slots__ 을 이용해서 attributes 값 고정!
- 속도가 미미하게 빨라진다라는.. 
- [소스코드](8.slots.py)

#### 9. Python Nitpicks
- Python의 유용한 문법 트릭들
  - For-else 구문: 반복문에서 특정 조건을 찾는 경우에 유용
  - Walrus 연산자 (:=): 변수 할당과 조건문을 동시에 사용
  - Short-circuit evaluation: 체인 구조로 None 체크
  - Operator Chaining: 여러 조건을 한 줄로 작성
- [소스코드](9.python_nitpicks.py)

#### 10. Advanced f-string String Formatting
#### 11. Cache / lru_cache

#### 12. Python Futures
- 비동기 프로그래밍을 위한 Future 객체 사용법
  - Promise와 유사한 비동기 연산 제어
  - 콜백 함수 첨부 가능
  - Exception 처리와 Timeout 설정
  - ThreadPoolExecutor와의 통합 사용
- [소스코드](12.python_futures.py)

#### 13. Proxy Properties
#### 14. Metaclasses

#### 15. NamedTuple vs Dataclass?
- NamedTuple 은 언제 쓰면 좋을까?
- 사실상 Dataclass로 퉁쳐도 되는게 아닐까?
- 그럼에도 아주 간단한 class 만들땐 괜찮을 듯
- 결국 collection.namedTuple(...) 과 동일.
- [소스코드](15.named_tuple.py)