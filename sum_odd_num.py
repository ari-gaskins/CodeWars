def row_sum_odd_numbers(n):
    n = int(n)
    term = int(n * (n + 1)/2)
    print('The ' + str(n) + 'th term is ' + str(term))

num = input('Enter n value: ')

row_sum_odd_numbers(num)