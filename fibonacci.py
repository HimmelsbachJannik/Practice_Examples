def printFibonacciSequence(num):
    fib_1 = 0
    fib_2 = 1
    fib_step = 2

    if num <= 0:
        print('Input not valid!')
    elif num == 1:
        print(0)
    else:
        print(fib_1)
        print(fib_2)
        while fib_step < num:
            fib_new = fib_1 + fib_2
            print(fib_new)
            fib_1 = fib_2
            fib_2 = fib_new
            fib_step += 1


'''Manual Tests'''
printFibonacciSequence(12)
