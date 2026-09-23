def num_count(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count
print(num_count(124567))