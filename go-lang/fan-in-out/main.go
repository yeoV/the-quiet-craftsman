package main

import (
	"fmt"
	"sync"
)

func generate(nums ...int) <-chan int {
	out := make(chan int)
	go func() {
		for _, n := range nums {
			out <- n
		}
		close(out)
	}()
	return out
}

func squareWorker(in <-chan int) <-chan int {
	out := make(chan int)
	go func() {
		for n := range in {
			out <- n * n
		}
		close(out)
	}()
	return out
}

func merge(cs ...<-chan int) <-chan int {
	var wg sync.WaitGroup
	out := make(chan int)

	// 열린 채널 만큼
	wg.Add(len(cs))
	for _, c := range cs {
		go func(c <-chan int) {
			defer wg.Done()
			for n := range c {
				out <- n
			}
		}(c)
	}

	go func() {
		wg.Wait()
		close(out)
	}()
	return out
}

func main() {

	numsSlice := make([]int, 100)
	for i := range numsSlice {
		numsSlice[i] = i + 1
	}
	nums := generate(numsSlice...)

	worker1 := squareWorker(nums)
	worker2 := squareWorker(nums)
	worker3 := squareWorker(nums)

	merged := merge(worker1, worker2, worker3)

	for result := range merged {
		fmt.Println("Result:", result)
	}
}
