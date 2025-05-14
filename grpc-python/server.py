import grpc
import logging
from concurrent import futures 

import echo_pb2
import echo_pb2_grpc 


class EchoerServicer(echo_pb2_grpc.echoerServicer):

    def SayEcho(self, request_iterator, context):
        for chunk in request_iterator:
            yield echo_pb2.echoResponse(echo_text="echo from server : " + chunk.text)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    echo_pb2_grpc.add_echoerServicer_to_server(
        EchoerServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()