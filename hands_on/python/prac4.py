# factorial and fibonacci series

def factorial(val):
    tmp = 1
    for i in range(1, val + 1):
        tmp *= i
    print(f"Factorial of the given number is : {tmp}")


def fibonacci(val):
    tmp = []
    for i in range(val):
        if i < 2:
            num = i
        else:
            num = tmp[i - 1] + tmp[i - 2]
        tmp.append(num)
    print(f"Fibonacci series is : {tmp}")


def main():
    try:
        val = int(input("Enter the number :"))
        factorial(val)
        fibonacci(val)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
