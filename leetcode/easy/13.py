def roman_to_int(s: str) -> int:
    result = i = 0
    symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    while i < len(s):
        if len(s) - i != 1:
            if symbols[s[i]] < symbols[s[i + 1]]:
                result = result + symbols[s[i + 1]] - symbols[s[i]]
                i += 2
            else:
                result = result + symbols[s[i]]
                i += 1
        else:
            result = result + symbols[s[-1]]
            break
    return result
