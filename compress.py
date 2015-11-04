'''Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3B1C2D4'.
 Only compress the string if it saves space.

 Constraints
-Can we assume the string is ASCII? Yes
-Can you use additional data structures? Yes
-Is this case sensitive? Yes

Test Cases:
None -> None
'' -> ''
'AABBCC' -> 'AABBCC'
'AAABCCDDDD' -> 'A3B1C2D4'    '''




def compress_string(string):
    if string is None or len(string)==0:
        return string

    counter = 0
    last_char = string[0]
    compressed_list = list()
    for char in string:

        if (char == last_char):
            counter = counter + 1
            last_char = char
        else:
            compressed_list.append(last_char)
            compressed_list.append(str(counter))
            counter = 1
            last_char = char

    compressed_list.append(last_char)
    compressed_list.append(str(counter))


    compressed_string = ''.join(compressed_list)

    #Testing if the compressed string is correct
    #print compressed_string


    if (len(compressed_string)<len(string)):
        return compressed_string
    else: return string


    pass

print compress_string("AAABCCDDDD")
print compress_string(None)
print compress_string("AABBCC")
print compress_string("")

