# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_result(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Result: {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def square(x):
    return x * x;

# fib0 = 0, fib1 = 1, fib2 = 1, fib3 = 2, fib4 = 3, fib5 = 5, fib6 = 8
def fib(n):
    """fib calculates n-th member
    of Fibonacci sequence"""

    a, b = 1, 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(1, n):
            a, b = b + a, a
        return a

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(0,10):
        print(f'{i} --> {fib(i)}')
    n = int(input('Enter N = '))
    print(fib(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
