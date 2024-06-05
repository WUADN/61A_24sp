def repeat_digits(n):
    last,rest = n % 10, n // 10
    if rest == 0:
        return last * 10 + last
    return repeat_digits(rest) * 100 + last

print(repeat_digits(1234))