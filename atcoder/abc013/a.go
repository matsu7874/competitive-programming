package main

import (
    "bufio"
    "fmt"
    "os"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
    var x string
    if sc.Scan() {
        x = sc.Text()
    }
    if x == "A"{
        fmt.Println(1)
    }else if x == "B"{
        fmt.Println(2)
    }else if x == "C"{
        fmt.Println(3)
    }else if x == "D"{
        fmt.Println(4)
    }else if x == "E"{
        fmt.Println(5)
    }
}