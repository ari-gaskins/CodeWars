def row_sum_odd_numbers(n):
    term = int(n * (n + 2)/2)
    print(f'The {str(n)}th term is {str(term)}')

num = input('Enter n value: ')

row_sum_odd_numbers(num)