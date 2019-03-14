def nonrecursive_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)


print(recursive_factorial(5))
