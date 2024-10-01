use rand::Rng;
use std::cmp::Ordering;
use std::io;

const MAX_GUESSES_HISTORY: usize = 3;

fn get_type_name<T>(_: T) -> &'static str {
    return std::any::type_name::<T>();
}

fn print_array(arr: &mut [i32; MAX_GUESSES_HISTORY]) {
    print!("[");
    for i in 0..arr.len() {
        if arr[i] == -1 {
            break;
        }
        print!("{:?}, ", arr[i]);
    }
    print!("]\n");
}

fn if_condition(condition: bool) {
    let number = if condition {5} else {6};
    println!("condition: {}, number: {}", condition, number);
}

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    str_len();
    if_condition(true);
    if_condition(false);

    let mut last_guesses: [i32; MAX_GUESSES_HISTORY] = [-1, -1, -1];
    let mut i = 0;
    let last_guess = loop {
        
        println!("Input your guess:");
        let mut guess = String::new();

        io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");
        
        let guess: i32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => { println!("Parsing error, input: {guess}"); continue; }
        };

        println!("Now the guess is: {guess}, type: {}", get_type_name(guess));

        match guess.cmp(&secret_number) {
            Ordering::Equal => {
                println!("You win!");
                break guess;
            },
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too large!"),
        }

        last_guesses[i] = guess;
        i += 1;
        i %= MAX_GUESSES_HISTORY;
        print!("Your last {MAX_GUESSES_HISTORY} guesses: " );
        print_array(&mut last_guesses);
    };

    println!("The last guess is: {}", last_guess);
}


fn str_len() {
    let spaces = "     ";
    let spaces = spaces.len();
    println!("spaces: {}", spaces);
}
