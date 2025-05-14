package main

import (
	"context"
	"flag"
	"io"
	"log"
	"time"

	pb "grpc-golang/echo"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

var (
	serverAddr = flag.String("addr", "localhost:50051", "Server Address")
)

func runSayEcho(client pb.EchoerClient) {
	notes := []*pb.EchoRequest{
		{Text: "Hello"},
		{Text: "World"},
		{Text: "I'm"},
		{Text: "Your"},
		{Text: "Man"},
	}
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	stream, err := client.SayEcho(ctx)
	if err != nil {
		log.Fatalf("client.SayEcho failed: %v", err)
	}
	waitc := make(chan struct{})
	// Server Response
	go func() {
		for {
			in, err := stream.Recv()
			if err == io.EOF {
				close(waitc)
				return
			}
			if err != nil {
				log.Fatalf("client.SayEcho failed: %v", err)

			}
			log.Printf("Got message : %s", in.EchoText)

		}
	}()

	//Server Request
	for _, req := range notes {
		if err := stream.Send(req); err != nil {
			log.Fatalf("SayEcho failed. stream.Send(%v), faield : %v", req, err)
		}
	}
	stream.CloseSend()
	<-waitc // close 시그널 wait
}

func main() {
	flag.Parse()

	opts := []grpc.DialOption{
		grpc.WithTransportCredentials(insecure.NewCredentials()),
	}
	conn, err := grpc.NewClient(*serverAddr, opts...)
	if err != nil {
		log.Fatal("Conncection Error. %v", err)
	}
	defer conn.Close()

	client := pb.NewEchoerClient(conn)
	runSayEcho(client)

}
