import random
import sys

operations = ['+', '-', '*', '/']

def generate_expression():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    operation = random.choice(operations)
    return f"{num1}{operation}{num2}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: generator <number_of_expressions>")
        sys.exit(1)

    num_expressions = int(sys.argv[1])
    for _ in range(num_expressions):
        print(generate_expression())
