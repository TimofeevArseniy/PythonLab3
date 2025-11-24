n = int(input("Введите количество чисел Фибоначчи: "))

if n <= 0:
    print("Введите положительное число.")
else:
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    print("Первые", n, "чисел Фибоначчи:")
    print(fib[:n])