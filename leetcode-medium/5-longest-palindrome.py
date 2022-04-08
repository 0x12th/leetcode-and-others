def palindromeAt(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]


def longestPalindrome_1(s):
    res = s[0]
    for i in range(len(s)):
        odd = palindromeAt(s, i, i)
        even = palindromeAt(s, i, i + 1)
        res = max(res, odd, even, key=len)
    return res


def longestPalindrome_2(s):
    res = s[0]
    for i in range(len(s)):
        for j in range(len(s) - 1, i - 1, -1):
            if s[i] == s[j]:
                m = s[i:j + 1]
                if m == m[::-1] and len(res) <= len(m):
                    res = m
    return res
