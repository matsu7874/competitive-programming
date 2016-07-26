package main

import "fmt"

func main() {
	var a, b, c int
	ret := "NO"
	fmt.Scan(&a, &b, &c)
	if a == 7 {
		if b == 5 && c == 5 {
			ret = "YES"
		}
	} else if b == 7 {
		if a == 5 && c == 5 {
			ret = "YES"
		}
	} else if c == 7 {
		if b == 5 && a == 5 {
			ret = "YES"
		}
	}
	fmt.Println(ret)
}
