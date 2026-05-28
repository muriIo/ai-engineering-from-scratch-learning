const GLOBAL_CONST: i8 = 30;
static FIRST_STATIC_VARIABLE: i8 = 21;

fn main() {
    let x = 5;

    println!("The value of x is: {}", x);

    let x = x + 1;

    let x = x * 2;

    println!("The value of x is: {}", x);

    let spaces = "    ";

    println!("Space as text: {} finished.", spaces);

    let spaces = spaces.len();

    println!("The length of spaces is {}", spaces);

    println!("The global const can be use here at main: {}", GLOBAL_CONST);

    println!(
        "The static variable can be use here at main: {}",
        FIRST_STATIC_VARIABLE
    );

    print_constants_and_statics();
}

fn print_constants_and_statics() {
    println!(
        "The global const can be use here at printConstantsAndStatics: {}",
        GLOBAL_CONST
    );

    println!(
        "The static variable can be use here at printConstantsAndStatics: {}",
        FIRST_STATIC_VARIABLE
    );

    const LOCAL_CONST: i8 = 55;

    println!(
        "The local const can only be use here at printConstantsAndStatics: {}",
        LOCAL_CONST
    );
}
