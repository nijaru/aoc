use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::path::Path;

fn read_input<P: AsRef<Path>>(filename: P) -> io::Result<Vec<Vec<char>>> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let grid: Vec<Vec<char>> = reader
        .lines()
        .map(|line| line.unwrap().chars().collect())
        .collect();

    Ok(grid)
}

fn find_target_points(grid: &Vec<Vec<char>>, target: char) -> Vec<(usize, usize)> {
    let mut target_points = Vec::new();

    for (i, row) in grid.iter().enumerate() {
        for (j, &cell) in row.iter().enumerate() {
            if cell == target {
                target_points.push((i, j));
            }
        }
    }

    target_points
}

fn check_sequence(grid: &Vec<Vec<char>>, row: isize, col: isize, dr: isize, dc: isize) -> bool {
    let rows = grid.len() as isize;
    let cols = grid[0].len() as isize;

    let coords = [(row + dr, col + dc), (row, col), (row - dr, col - dc)];

    for &(r, c) in &coords {
        if r < 0 || r >= rows || c < 0 || c >= cols {
            return false;
        }
    }

    let chars: Vec<char> = coords
        .iter()
        .map(|&(r, c)| grid[r as usize][c as usize])
        .collect();

    (chars[0] == 'M' && chars[1] == 'A' && chars[2] == 'S')
        || (chars[0] == 'S' && chars[1] == 'A' && chars[2] == 'M')
}

fn count_xmas(grid: &Vec<Vec<char>>) -> usize {
    let a_points = find_target_points(grid, 'A');
    let mut count = 0;

    let diagonals = vec![(-1, -1), (-1, 1)];

    for &(i, j) in &a_points {
        let mut valid = true;

        for &(dr, dc) in &diagonals {
            if !check_sequence(grid, i as isize, j as isize, dr, dc) {
                valid = false;
                break;
            }
        }

        if valid {
            count += 1;
        }
    }

    count
}

fn main() -> io::Result<()> {
    let grid = read_input("input.txt")?;

    let xmas_count = count_xmas(&grid);

    println!("Total 'X-MAS' occurrences found: {}", xmas_count);

    Ok(())
}
