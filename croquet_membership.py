# categorize members into 'senior' or 'open'
# senior is age 55+ with a handicap > 7
# open is everyone not categorized as a senior

def open_or_senior(data):
    memberships = []
    for i in range(len(data)):
        members = data[i]
        age = members[:1]
        for i in range(len(age)):
            age = age[i]
        handicap = members[1:]
        for i in range(len(handicap)):
            handicap = handicap[i]
        if age >= 55 and handicap > 7:
            memberships.append('Senior')
        else:
            memberships.append('Open')
    return memberships


print(open_or_senior([[18, 20], [45, 2], [61, 12]]))

#def list_of_strings(answer):
#    list = []
#    yes = 'y'
#    no = 'n'
#    if answer is yes:
#        list.append(yes)
#    else:
#        list.append(no)
#    print(list)

#list_of_strings('y')
#list_of_strings('n')
#list_of_strings('n')

#def sliced_list(data):
#    age = data[:1]
#    handicap = data[1:]
#    print(age)
#    print(handicap)


#sliced_list([18, 20])
#sliced_list([45, 2])