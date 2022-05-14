# given two unsorted strings of varying letter frequency,
# return a string with a combination of all letters 
# with only one of each distinct letter
# and sorted alphabetically

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

def longest(s1, s2):
    return s1 + s2


def one_of_each(s1):
    str_list = []
    str_list[:0] = s1
    str_list = sorted(str_list)
    for i in range(len(str_list)):
        if i not in str_list:
            str_list.append(i)
    print(str_list)


one_of_each(a)
one_of_each(b)

#def string_to_list(s1):
#    str_list = []
#    str_list[:0] = s1
#    print(str_list)

#string_to_list(a)
#string_to_list(b)
