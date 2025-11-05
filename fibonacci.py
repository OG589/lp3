def fib_iterative(n):
    a, b = 0, 1
    print(f"Fibonacci sequence up to {n} terms (Iterative): ", end="")

    if n >= 1:
        print(a, end=" ")
    if n >= 2:
        print(b, end=" ")

    for _ in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c
n = int(input("Enter number of terms: "))
fib_iterative(n)
print()
###


def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


n = int(input("Enter number of terms: "))
print(f"Fibonacci sequence up to {n} terms (Recursive): ", end="")

for i in range(n):
    print(fib_recursive(i), end=" ")
