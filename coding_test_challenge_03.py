def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    count = 0

    len_s = len(s) #lentgh of s 
    # index 0, 1
    for index in range(len_s):
        #  index = 0 (first iteration), (2nd iteration) index = 1
        if index!=len(s)-1 and roman.get(s[index]) < roman.get(s[index+1]): # I (index = 0) < V (index = 1), (2nd iteration) V (index = 1) ? index + 1
            each_char = s[index]
            value = roman.get(each_char)
            count = count - value
        else:
            each_char = s[index]
            value = roman.get(each_char)
            count = count + value

    print("final answer", count)

print(romanToInt("IVI"))