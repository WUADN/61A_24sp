def repeat_digits(n):
    """
    Given a positive integer N, returns a number with each digit repeated.
    >>> repeat_digits(1234)
    11223344
    """
    last,rest = n % 10, n // 10
    if rest == 0:
        return last * 10 + last
    return repeat_digits(rest) * 100 + last * 10 + last
repeat_digits(1234)

