import grpc
import echo_pb2
import echo_pb2_grpc


def request_generator():
    texts = "Hello world, i'm also developer.".split()
    for t in texts:
        yield echo_pb2.echoRequest(text=t)

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = echo_pb2_grpc.echoerStub(channel)
        
        # cluent stream으로 데이터 집어 넣음
        responses = stub.SayEcho(request_generator())
        for resp in responses:
            print("Server 응답 :", resp.echo_text)


if __name__ == "__main__":
    run()
