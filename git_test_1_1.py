
def fib(n):
    # 1, 1, 2, 3, 5, 8, 13
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
        print(b)
    pass


if __name__ == "__main__":
    fib(10)


