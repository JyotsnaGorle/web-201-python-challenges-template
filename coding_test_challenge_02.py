def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    rev = 0
    dup = x
    while(x>0):
        dig = x%10
        rev = rev*10 + dig
        x = x//10
    if rev == dup:
        return True
    return False


def test_challenge_07_happy_case(): 
    assert isPalindrome(121) == True


