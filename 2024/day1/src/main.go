package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	a := make([]int, 0, 1000)
	b := make([]int, 0, 1000)

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		num1, _ := strconv.Atoi(fields[0])
		num2, _ := strconv.Atoi(fields[1])
		a = append(a, num1)
		b = append(b, num2)
	}

	sort.Ints(a)
	sort.Ints(b)

	sum := 0

	for i := 0; i < len(a); i++ {
		sum += int(math.Abs(float64(a[i] - b[i])))
	}

	fmt.Println(sum)
}
