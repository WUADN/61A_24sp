def max_product(s):
    """这段代码是未改进的代码
    Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(s) == 0:
        return 1
    if len(s) == 1:
        return s[0]
    if len(s) == 2:
        return max(s[0], s[1])
    if len(s) == 3:
        return max(s[0] * s[2], s[1])
    if len(s) == 4:
        return max(max(s[0] * s[2]* s[4], s[0] * s[4]), max(s[1] * s[3], s[1] * s[4]))
    if s[0] * s[2] < s[1]:
        return max_product(s[1:])
    if s[2] * s[4] < s[3]:
        return s[0] * max_product(s[3:])
    return s[0] * max_product(s[2:])