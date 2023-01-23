def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    values = {}
    for idx, value in enumerate(nums):
        if target - value in values:
            return [values[target - value], idx]
        else:
            values[value] = idx

def test_challenge_07_happy_case(): 
    assert twoSum([2,7,11,15], 9) == [0,1]
