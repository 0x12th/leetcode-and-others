"""
fuzzysearch('car', 'cartwheel') # True
fuzzysearch('cwhl', 'cartwheel') # True
fuzzysearch('cwhoe', 'cartwheel') # True
fuzzysearch('cartwheel', 'cartwheel') # True
fuzzysearch('cwheeel', 'cartwheel') # False
fuzzysearch('lw', 'cartwheel') # False
"""


def fuzzysearch(pattern: str, text: str) -> bool:
    if not pattern:
        return True
    if len(pattern) > len(text):
        return False

    i = 0
    for ch in text:
        if ch == pattern[i]:
            i += 1
            if i == len(pattern):
                return True

    return False
