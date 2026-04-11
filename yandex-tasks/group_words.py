"""
["eat", "tea", "tan", "ate", "nat", "bat"] ->
[["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
"""

from collections import defaultdict


def group_words(words: list[str]) -> list[list[str]]:
    group: defaultdict[str, list] = defaultdict(list)
    for word in words:
        group[str(sorted(word))].append(word)
    return [sorted(words) for words in group.values()]
