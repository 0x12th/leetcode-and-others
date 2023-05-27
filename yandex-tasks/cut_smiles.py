"""
some:-)thing -> something
some:-)))thing -> something
some:-)th:-))ing -> something
:-)( -> (
"""


def cut_smile(s: str) -> str:
    cnt = 0
    result = []
    while cnt <= len(s) - 1:
        if s[cnt] == ":" and s[cnt + 1] == "-" and s[cnt + 2] in (")", "("):
            bracket = s[cnt + 2]
            cnt_bracket = cnt + 2
            while cnt_bracket <= len(s) - 1:
                if s[cnt_bracket] != bracket:
                    result.append(s[cnt_bracket])
                    break
                else:
                    cnt_bracket += 1
            cnt = cnt_bracket
        else:
            result.append(s[cnt])
        cnt += 1
    return "".join(result)
