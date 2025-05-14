package main

import (
	"flag"
	"fmt"
	pb "grpc-golang/echo"
	"io"
	"log"
	"net"

	"google.golang.org/grpc"
)

var (
	port = flag.Int("port", 50051, "The server port")
)

type server struct {
	pb.UnimplementedEchoerServer
}

func serialize(req *pb.EchoRequest) string {
	return fmt.Sprintf("Echo server : %s", req.Text)
}

func (s *server) SayEcho(stream pb.Echoer_SayEchoServer) error {
	for {
		in, err := stream.Recv()
		if err == io.EOF {
			return nil
		}
		if err != nil {
			return err
		}
		out := pb.EchoResponse{
			EchoText: serialize(in),
		}
		stream.Send(&out)

	}

}
func newServer() *server {
	s := &server{}
	return s

}

func main() {
	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf("localhost:%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	var opts []grpc.ServerOption

	grpcServer := grpc.NewServer(opts...)
	pb.RegisterEchoerServer(grpcServer, newServer())
	grpcServer.Serve(lis)
}
