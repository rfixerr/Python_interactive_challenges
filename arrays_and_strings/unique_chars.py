'''Implement an algorithm to determine if a string has all unique characters

    Constraints
        Can you assume the string is ASCII? Yes
        Can we assume this is case sensitive? Yes
        Can you use additional data structures? Yes

    Test Cases
        '' -> True
        'foo' -> False
        'bar' -> True'''


def unique_chars(string):
    if len(string) == 0:
        return True
    last_char = string[0]
    counter = 0
    for char in string:
        if char == last_char:
            counter= counter + 1
            last_char = char
            if counter > 1:
                return False
        else:
            last_char = char
    return True


#Tests
print unique_chars('foo')
print unique_chars('abc')
print unique_chars('aaabb')
print unique_chars('aa')
print unique_chars('1233')
print unique_chars('')