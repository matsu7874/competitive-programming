package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	var length, n int
	fmt.Scan(&n, &length)
	var s []string
	var tmp string
	for i := 0; i < n; i++ {
		fmt.Scan(&tmp)
		s = append(s, tmp)
	}
	sort.Strings(s)
	fmt.Println(strings.Join(s, ""))
}
