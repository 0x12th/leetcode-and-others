# Напишите функцию, которая проверит строку на сбалансированность скобок: {}, (), [].
# Вернуть true если они сбалансированы, иначе false.
# '(x + y) - (4)' -> true
# '(((10 ) ()) ((?)(:)))' -> true
# '[{()}]' -> true
# '(50)(' -> false
# '[{]}' -> false


def is_balanced_brackets(s: str) -> bool:
    st = []
    dct = {"{": "}", "(": ")", "[": "]"}
    for br in s:
        if br in dct:
            st.append(br)
        else:
            if len(st) == 0 or br != dct[st.pop()]:
                return False
    return len(st) == 0
