def fibonacci(num):
    fib_1 = 0
    fib_2 = 1
    i = 0

    if num <= 0:
        print('Input not valid!')
    elif num == 1:
        print(0)
    else:
        print(fib_1)
        print(fib_2)
        while i <= num:
            fib_new = fib_1 + fib_2
            print(fib_new)
            fib_1 = fib_2
            fib_2 = fib_new
            i += 1


'''Manual Tests'''
# fibonacci(11)
