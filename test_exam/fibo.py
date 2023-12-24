def generate_fibonacci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence


n = 10
fib_series = generate_fibonacci(n)
print(f"Fibonacci series of length {n}: {fib_series}")
