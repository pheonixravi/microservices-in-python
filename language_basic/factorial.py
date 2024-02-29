def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

number=5
print("Factorial of", number, ":", factorial(number))
