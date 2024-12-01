fn main() {
    let input = std::fs::read_to_string("input.txt").unwrap();

    let mut vec1 = Vec::new();
    let mut vec2 = Vec::new();
    for line in input.lines() {
        let mut split = line.split_whitespace();
        let num1: i32 = split.next().unwrap().parse().unwrap();
        let num2: i32 = split.next().unwrap().parse().unwrap();
        vec1.push(num1);
        vec2.push(num2);
    }

    vec1.sort();
    vec2.sort();

    let mut sum = 0;
    for i in 0..vec1.len() {
        sum += (vec1[i] - vec2[i]).abs();
    }

    // print sum
    println!("{}", sum);
}
