# gRPC Go Example

간단한 gRPC Go 예제 프로젝트입니다.

## 프로젝트 구조

- `echo/`: Protocol Buffer 정의 및 생성된 코드
- `client/`: gRPC 클라이언트 코드
- `server/`: gRPC 서버 코드

## 설치 및 실행 방법

### 1. 필수 도구 설치

프로젝트를 실행하기 위해서는 다음과 같은 도구들이 필요합니다:

```bash
# Go 설치 (최신 버전 권장)
# Homebrew를 사용하여 설치
brew install go

# Protocol Buffers 컴파일러 설치
brew install protobuf

# gRPC Go 플러그인 설치
brew install grpc
```

### 2. 의존성 설치

```bash
go get google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
export PATH="$PATH:$(go env GOPATH)/bin"
go mod tidy
```

### 3. gRPC 서비스 생성

프로젝트의 `echo.proto` 파일을 기반으로 gRPC 서비스 코드를 생성합니다:

```bash
protoc --go_out=. --go-grpc_out=. ./echo/echo.proto
```

### 4. 서버 실행

서버를 실행하기 전에 서버 디렉토리로 이동합니다:

```bash
cd ./server
# 서버 실행
go run server.go
```

### 5. 클라이언트 실행

서버가 실행 중일 때 클라이언트를 실행할 수 있습니다:

```bash
cd ./client
# 클라이언트 실행
go run client.go
```

## 프로젝트 구조 상세

- `echo/echo.proto`: gRPC 서비스 정의 파일
- `echo/echo.pb.go`: Protocol Buffer 메시지 정의
- `echo/echo_grpc.pb.go`: gRPC 서비스 인터페이스
- `server/server.go`: gRPC 서버 구현
- `client/client.go`: gRPC 클라이언트 구현

## 주의사항

- 서버를 먼저 실행한 후 클라이언트를 실행해야 합니다.
- 프로토콜 버퍼 파일이 변경된 경우 `protoc` 명령어를 다시 실행하여 코드를 재생성해야 합니다.
- Go 1.23.4 이상이 필요합니다.

#### 참고
https://grpc.io/docs/languages/go/basics/