# abacbc
# a - dict something - {'a': 1}
# b - {'a': 1, 'b': 1}
# a - check if in something === true {'a': 2, 'b': 1}
# c - {'a': 2, 'b': 1, 'c': 1}

def areOccurrencesEqual(s):
    values_dict = {}
    for each in s:
        if each not in values_dict:
            values_dict[each] = 1
        else:
            values_dict[each] = values_dict[each] + 1
    first_freq = values_dict[s[0]] # 2
    for k in values_dict:
        if first_freq != values_dict[k]:
            return False
    return True

print(areOccurrencesEqual("abacbc"))

