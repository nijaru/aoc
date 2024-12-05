package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

func validDiff(num1, num2 int) bool {
	diff := math.Abs(float64(num1 - num2))
	return diff >= 1 && diff <= 3
}

func isValidSequence(nums []int) bool {
	if len(nums) < 2 {
		return false
	}

	ascending := nums[1] > nums[0]

	for i := 1; i < len(nums); i++ {
		current, previous := nums[i], nums[i-1]

		if current == previous {
			return false
		}

		if ascending && current < previous {
			return false
		}
		if !ascending && current > previous {
			return false
		}

		if !validDiff(current, previous) {
			return false
		}
	}

	return true
}

func parseLines(lines []string) ([][]int, error) {
	parsed := make([][]int, 0, len(lines))
	for _, line := range lines {
		fields := strings.Fields(line)
		nums := make([]int, len(fields))
		for i, field := range fields {
			num, err := strconv.Atoi(field)
			if err != nil {
				return nil, fmt.Errorf("error parsing integer: %v", err)
			}
			nums[i] = num
		}
		parsed = append(parsed, nums)
	}
	return parsed, nil
}

func part1(sequences [][]int) int {
	count := 0
	for _, nums := range sequences {
		if isValidSequence(nums) {
			count++
		}
	}
	return count
}

func part2(sequences [][]int) int {
	count := 0
	for _, nums := range sequences {
		if isValidSequence(nums) {
			count++
			continue
		}

		valid := false
		for i := range nums {
			testNums := append(nums[:i], nums[i+1:]...)
			if isValidSequence(testNums) {
				valid = true
				break
			}
		}

		if valid {
			count++
		}
	}
	return count
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalf("Failed to open file: %v", err)
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line != "" {
			lines = append(lines, line)
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatalf("Error reading file: %v", err)
	}

	sequences, err := parseLines(lines)
	if err != nil {
		log.Fatalf("Error parsing lines: %v", err)
	}

	fmt.Println(part1(sequences))
	fmt.Println(part2(sequences))
}
