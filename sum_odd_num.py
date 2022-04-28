def row_sum_odd_numbers(n):
    n = int(n)
    digit = 1
    for i in range(n, 7):
        n = i
        term = int(n * (n + 1)/2)
        digit +=2
        print(f'For the {str(n)}th term of {str(term)} the digit is {str(digit)}')
        

num = input('Enter n value: ')

row_sum_odd_numbers(num)