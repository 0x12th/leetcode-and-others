"""
Дана строка, состоящая из букв ‘X’, ‘Y’ и ‘0’. Необходимо найти кратчайшее расстояние между буквами ‘X’ и ‘Y’, либо вывести 0, если ‘X’ либо ‘Y’ отсутствуют.

"YY" -> 0
"XX" -> 0
"XY" -> 1
"YOX" -> 2
"000X00Y0X0X0" -> 2
"000XX0Y" -> 2
"""


def min_distance_xy(s: str) -> int:
    res = len_s = len(s)
    last_pos, last_ch = -1, ""

    for i in range(len_s):
        ch = s[i]
        if ch == "0":
            continue
        if last_pos != -1 and ch != last_ch:
            dist = i - last_pos
            if dist < res:
                if dist == 1:
                    return 1
                res = dist
        last_pos, last_ch = i, ch

    return 0 if res == len_s else res
