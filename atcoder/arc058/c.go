package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func nextInt() uint32 {
	sc.Scan()
	i, e := strconv.Atoi(sc.Text())
	if e != nil {
		panic(e)
	}
	return uint32(i)
}

func convertDigitsBits(n uint32) uint32 {
	var ret uint32
	for ; n > 0; n /= 10 {
		ret = ret | 1<<(n%10)
	}
	return ret
}
func main() {
	sc.Split(bufio.ScanWords)
	n, k := nextInt(), int(nextInt())
	var pattern uint32
	for i := 0; i < k; i++ {
		pattern += (1 << nextInt())
	}
	for i := n; ; i++ {
		if convertDigitsBits(i)&pattern == 0 {
			fmt.Println(i)
			break
		}
	}
}
