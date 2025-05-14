# gRPC Python Example

간단한 gRPC Python 예제 프로젝트입니다. 이 프로젝트는 클라이언트-서버 간의 양방향 스트리밍 통신을 구현한 예제입니다.

## 프로젝트 구조

- `echo.proto`: Protocol Buffer 정의 파일 (양방향 스트리밍 서비스 정의)
- `client.py`: gRPC 클라이언트 코드 (스트리밍 요청 생성 및 처리)
- `server.py`: gRPC 서버 코드 (스트리밍 응답 처리)
- `echo_pb2.py`, `echo_pb2_grpc.py`: Protocol Buffer로 생성된 코드
- `pyproject.toml`: Python 패키지 설정 파일

## 설치 및 실행 방법

### 1. Python 환경 설정

```bash
uv sync --all-extras --frozen
```



### 2. Protocol Buffer 파일 생성

프로토콜 버퍼 파일을 기반으로 Python 코드를 생성합니다:

```bash
# Protocol Buffer 컴파일러 설치
pip install grpcio-tools

```

- generate grpc code
``` bash
uv run python -m grpc_tools.protoc \
--proto_path=. \
--python_out=. \
--grpc_python_out=. \
./echo.proto

```

### 3. 서버 실행

```bash
# 서버 실행
python server.py
```

### 4. 클라이언트 실행

서버가 실행 중일 때 클라이언트를 실행할 수 있습니다:

```bash
# 클라이언트 실행
python client.py
```

## 프로토콜 정의

`echo.proto` 파일은 다음과 같은 서비스를 정의합니다:

- `echoer` 서비스: 양방향 스트리밍 RPC 서비스
- `SayEcho` 메소드: 클라이언트와 서버 간의 양방향 스트리밍 통신
- `echoRequest`: 클라이언트가 보낼 텍스트 메시지
- `echoResponse`: 서버가 보낼 응답 메시지

## 실행 예시

1. 먼저 서버를 실행합니다:
```bash
python server.py
```

2. 새로운 터미널에서 클라이언트를 실행합니다:
```bash
python client.py
```

클라이언트는 "Hello world, i'm also developer."를 단어별로 서버에 전송하고, 서버는 각 단어에 대해 "echo from server : [단어]" 형태의 응답을 반환합니다.

## 주의사항

- 서버를 먼저 실행한 후 클라이언트를 실행해야 합니다.
- 프로토콜 버퍼 파일이 변경된 경우 `python -m grpc_tools.protoc` 명령어를 다시 실행하여 코드를 재생성해야 합니다.
- 서버는 50051 포트에서 실행됩니다.