#!/usr/bin/env sh

function aoc-input () {
	local session_cookie=${1:-$AOC_SESSION}
	if [ -z "$session_cookie" ]; then
        echo "Please provide a session cookie or set the AOC_SESSION environment variable"
        return 1
    fi
	day=$(basename $(pwd) | tr -dc '0-9')
	curl --cookie "session=$session_cookie" "https://adventofcode.com/2024/day/$day/input" > input.txt
}

aoc-input $1
