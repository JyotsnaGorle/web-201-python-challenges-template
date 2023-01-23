
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    subs = s[0]
    
    max = 0
    for i in range(1, len(s)):
        if s[i] not in subs:
            subs = subs + s[i]
        else:
            if (len(subs) > max):
                max = len(subs)
            subs = ""
    return max   

def test_challenge_02_case_1(): 
     assert lengthOfLongestSubstring("abcabcbb") == 3