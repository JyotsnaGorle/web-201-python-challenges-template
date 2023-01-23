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
     elif i == len(s) - 1:
          if (len(subs) > max):
               max = len(subs)      
     else:
          if (len(subs) > max):
               max = len(subs)
          subs = ""
    return max

def test_challenge_02_case_1(): 
     assert lengthOfLongestSubstring("abcabcbb") == 3

def test_challenge_03_case_1(): 
     assert lengthOfLongestSubstring("pwwkew") == 3