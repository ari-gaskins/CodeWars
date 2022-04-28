def row_sum_odd_numbers(n):
    lst = []
    num = 1
    next_num = num 
    for i in range(1, n):
        next_num += i
        lst.append(next_num)
    for i in range(len(lst)):
        print(lst[i])

row_sum_odd_numbers(1)