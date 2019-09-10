# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the
# first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, find the sum of the even-valued terms.


def even_fibonacci(number):
    fib_list = []
    n = 0
    x = 1
    y = 2
    fib_list.append(x)
    fib_list.append(y)
    while n <= number - x:
        n = x + y
        fib_list.append(n)
        x = y
        y = n
    even_sum = 0
    for fib_n in fib_list:
        if fib_n % 2 == 0:
            even_sum += fib_n
    return even_sum


