package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func nextInt() int64 {
    sc.Scan()
    i, e := strconv.ParseInt(sc.Text(), 10, 64)
    if e != nil {
        panic(e)
    }
    return i
}

func main() {
    sc.Split(bufio.ScanWords)
    n := nextInt()
    m := nextInt()
    p := nextInt()
    var res int64 = 1
    for p>0{
        if p%2 == 1{
            res *= n
            res %= m
        }
        n = n*n%m
        p = p/2
    }
    fmt.Println(res)
}