"""
["eat", "tea", "tan", "ate", "nat", "bat"] ->
[["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
"""

from collections import defaultdict


def _group_words(words: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = {}

    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)

    return [sorted(group) for group in groups.values()]


def group_words(words: list[str]) -> list[list[str]]:
    group: defaultdict[str, list] = defaultdict(list)
    for word in words:
        group[str(sorted(word))].append(word)
    return [sorted(words) for words in group.values()]


print(_group_words(["eat", "tea", "tan", "ate", "nat", "bat"]))
