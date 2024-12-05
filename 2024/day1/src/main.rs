fn main() {
    let input = std::fs::read_to_string("input.txt").unwrap();

    let mut vec1 = Vec::with_capacity(1000);
    let mut vec2 = Vec::with_capacity(1000);

    for line in input.lines() {
        let mut split = line.split_whitespace();
        let num1 = split.next().unwrap().parse::<i32>().unwrap();
        let num2 = split.next().unwrap().parse::<i32>().unwrap();
        vec1.push(num1);
        vec2.push(num2);
    }

    vec1.sort_unstable();
    vec2.sort_unstable();

    let sum: i32 = vec1
        .iter()
        .zip(vec2.iter())
        .map(|(a, b)| (a - b).abs())
        .sum();

    println!("{}", sum);
}
