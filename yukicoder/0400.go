package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	fmt.Scan(&s)
	size := len(s)
	var ret [20]string
	for i := 0; i < size; i++ {
		if s[size-i-1] == '<' {
			ret[i] = ">"
		} else {
			ret[i] = "<"
		}
	}
	fmt.Println(strings.Join(ret[0:size], ""))
}
