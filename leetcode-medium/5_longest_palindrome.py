def palindrome_at(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1: right]


def longest_palindrome_1(s):
    res = s[0]
    for i in range(len(s)):
        odd = palindrome_at(s, i, i)
        even = palindrome_at(s, i, i + 1)
        res = max(res, odd, even, key=len)
    return res


def longest_palindrome_2(s):
    res = s[0]
    for i in range(len(s)):
        for j in range(len(s) - 1, i - 1, -1):
            if s[i] == s[j]:
                m = s[i: j + 1]
                if m == m[::-1] and len(res) <= len(m):
                    res = m
    return res
