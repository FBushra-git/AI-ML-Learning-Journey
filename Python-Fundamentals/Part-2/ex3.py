def print_digit(n):
    while n > 0:
        digit = n % 10
        print(digit)
        n = n // 10
print_digit(12345)