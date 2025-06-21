def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(50)

def fibo(number):
    if number <= 1:
        return number
    return fibo(number - 1) + fibo(number - 2)

print(fibo(10))