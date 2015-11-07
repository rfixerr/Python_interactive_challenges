''' Determine if a string is a permutation of another string

    Constraints
        Can we assume the string is ASCII? Yes
        Is whitespace important? Yes
        Is this case sensitive? 'Nib', 'bin' is not a match? Yes

    Test Cases
        One or more empty strings -> False
        'Nib', 'bin' -> False
        'act', 'cat' -> True
        'a ct', 'ca t' -> True
'''

def permutations(str1, str2):

    if len(str1)!=len(str2) or str1 == '' or str2 =='':
        return False
    for char in str1:
        if not(char in str2):
            return False
    for char in str2:
        if not(char in str1):
            return False
    return True


print permutations('foo', 'oof')
print permutations('foo', 'oaf')
print permutations('oaf', 'foo')
print permutations('', '')
print permutations('a ct', 'ca t')
print permutations('acb', 'adc')