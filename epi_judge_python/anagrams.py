from collections import defaultdict
from typing import List, Dict

from test_framework import generic_test, test_utils
"""
Suppose you were asked to write a program that takes as input a set of words and returns groups
of anagrams for those words. Each group must contain at least two words.
For example, if the input is “debitcard”, “elvis”, “silent”, “badcredit”, “lives”, “freedom”,
“listen”, “levis”, “money” then there are three groups of anagrams: (1.) “debitcard”, “badcredit”;
(2.) “elvis”, “lives”, “levis”; (3.) “silent”, “listen”. (Note that “money” does not appear in any group,
since it has no anagrams in the set.)
"""

def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    anagrams: Dict[str, List[str]] = defaultdict(list)
    for word in dictionary:
        w: str = "".join(sorted(word)) # k = len(word) k.log(k)
        anagrams[w].append(word)
    return [words for key, words in anagrams.items() if len(words) >= 2]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
