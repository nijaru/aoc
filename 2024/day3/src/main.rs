fn main() {
    let input = std::fs::read_to_string("input.txt").unwrap();

    let section_re = regex::Regex::new(r#"(do\(\)|don't\(\))"#).unwrap();
    let sections = section_re.split(&input);

    let mut active = true;
    let mut total = 0;

    let mul_re = regex::Regex::new(r#"mul\s*\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)"#)
        .expect("Invalid multiplication regex");

    for section in sections {
        let section = section.trim();

        if section == "do()" {
            active = true;
        } else if section == "don't()" {
            active = false;
        } else {
            if active {
                for nums in mul_re.captures_iter(section) {
                    total += nums[1].parse::<i32>().unwrap() * nums[2].parse::<i32>().unwrap();
                }
            }
        }
    }

    println!("{}", total);
}
