
from operator import le
import re


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    # find the tiniest word
    # compare substrings from the tiniest word -
    # check is it exists in all other words
    print(strs)

    if len(strs) == 1:
        return strs[0]

    min_len_word = strs[0]
    min_len = len(strs[0])
    for each in strs:
        if len(each) < min_len:
            min_len = len(each)
            min_len_word = each
    print(min_len_word)

    substrings = []
    for i in range(len(min_len_word)):
        for j in range(i + 1, len(min_len_word) + 1):
            substrings.append(min_len_word[i:j])

    print(substrings)
    res = []
    for each_substring in substrings:
        count = 0
        for each_string in strs:
            if each_substring in each_string:
                count = count+1
        if count == len(strs):
            res.append(each_substring)

    if len(res) == 0:
        return ""
    if len(res) == 1:
        return res[0]

    max = 0
    longest_substring = ""
    for each in res:
        if len(each) > max:
            max = len(each)
            longest_substring = each
    return longest_substring


def test_challenge_07_happy_case(): 
    assert longestCommonPrefix(["flower","flow","flight"]) == "fl"

def test_challenge_08_happy_case(): 
    assert longestCommonPrefix(["dog","racecar","car"]) == ""

def test_challenge_09_happy_case(): 
    assert longestCommonPrefix(["s"]) == "s"

def test_challenge_09_happy_case(): 
    assert longestCommonPrefix(["cir", "car"]) == "c"
