"""
["eat", "tea", "tan", "ate", "nat", "bat"] ->
[["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
"""

from collections import defaultdict
from typing import DefaultDict, List


def group_words(words: List[str]) -> List[List[str]]:
    group: DefaultDict[str, list] = defaultdict(list)
    for word in words:
        group[str(sorted(word))].append(word)
    return [sorted(words) for words in group.values()]
