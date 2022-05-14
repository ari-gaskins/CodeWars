# given two unsorted strings of varying letter frequency,
# return a string with a combination of all letters 
# with only one of each distinct letter
# and sorted alphabetically

def longest(s1, s2):
    return s1 + s2


def string_to_list(s1):
    str_list = list(s1.split(''))
    print(str_list)

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

string_to_list(a)
string_to_list(b)
