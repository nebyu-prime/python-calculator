import argparse


def add(a: float, b: float) -> float:
    return a + b


def sub(a: float, b: float) -> float:
    return a - b


def mul(a: float, b: float) -> float:
    return a * b


def div(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


OPERATIONS = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
}


def calc_cli(operation: str, a: float, b: float) -> float:
    func = OPERATIONS[operation]
    return func(a, b)


def interactive():
    print("Simple Calculator (add, sub, mul, div)")
    print("Type 'q' to quit.")
    while True:
        choice = input("Operation [add/sub/mul/div or q]: ").strip().lower()
        if choice in ("q", "quit", "exit"):
            print("Goodbye!")
            break
        if choice not in OPERATIONS:
            print("Invalid operation. Try again.")
            continue
        try:
            a_str = input("Enter first number: ").strip()
            b_str = input("Enter second number: ").strip()
            a = float(a_str)
            b = float(b_str)
            result = OPERATIONS[choice](a, b)
            print(f"Result: {result}")
        except ValueError:
            print("Please enter valid numbers.")
        except ZeroDivisionError as e:
            print(e)


def main():
    parser = argparse.ArgumentParser(description="Simple Calculator")
    parser.add_argument("operation", nargs="?", choices=list(OPERATIONS.keys()), help="Operation to perform")
    parser.add_argument("a", nargs="?", type=float, help="First number")
    parser.add_argument("b", nargs="?", type=float, help="Second number")

    args = parser.parse_args()

    if args.operation is not None and args.a is not None and args.b is not None:
        try:
            result = calc_cli(args.operation, args.a, args.b)
            print(result)
        except ZeroDivisionError as e:
            print(e)
    else:
        interactive()


if __name__ == "__main__":
    main()
