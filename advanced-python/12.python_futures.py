# JS의 promise 같이 사용.비동기 연산을 직접 제어할 수 있음.! .then() 함수처럼 콜백 첨부 가능!

from concurrent.futures import Future

future = Future()

future.add_done_callback(lambda f: print(f"Got : {f.result()}"))

future.set_result("Async result")

future.add_done_callback(lambda f: print(f"After: {f.result()}"))

# Got : Async result
# After: Async result
# ------------------------------------------------------------------

# future에 exception 이나 timeout 등 기능 사용 가능
import time, threading

future = Future()

def background_task():
    time.sleep(2)
    future.set_result("Done")

thread = threading.Thread(target=background_task)
thread.daemon = True
thread.start()


print(f"Cancelled : {future.cancel()}") # task cancel

# timeout
try:
    result = future.result(timeout=0.5)
except TimeoutError:
    print("Timed out!")

err_future = Future()
err_future.set_exception(ValueError("Failed"))
print(f"Has error : {bool(err_future.exception())}")


# Cancelled : True
# Has error : True
# ------------------------------------------------------------------

# CPU, IO bound tasks의 경우, python ThreadPoolExcutor 는 자동으로 future를 create, manage 해줌
from concurrent.futures import ThreadPoolExecutor
import time

def slow_task():
    time.sleep(1)
    return "Done"

with ThreadPoolExecutor() as executor:
    # Future 바로 return
    future = executor.submit(slow_task)
    print(future)   # <Future at 0x10262f0e0 state=running>
    print(future.result())