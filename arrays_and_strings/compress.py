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


#  Algorithm
#
# If string is None or '' return string
# Create compressed list
# for char in string
#   if char equals last_char
#       increment counter
#       Assign last_char to char
#   else
#       Append last_char to compressed list
#       Append counter to compressed after converting it to a string
#       Reset counter to 1
#       Assign last_char to char
# Append last_char to compressed list
# Append counter to compressed after converting it to a string
# Convert compressed list to a string
# Testing to see which string has the shortest length
# If length(compressed_string) is shorter than length(string)
#   return compressed_string
# Else
#   return string


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

