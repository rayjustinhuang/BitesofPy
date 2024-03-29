import argparse

def calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
       
    if operation == 'add':
        return sum(numbers)
    elif operation == 'sub':
        running_total = numbers[0]
        for i in range(1, len(numbers)):
            running_total -= numbers[i]
        return round(running_total,2)
    elif operation == 'mul':
        running_total = numbers[0]
        for i in range(1, len(numbers)):
            running_total *= numbers[i]
        return round(running_total,2)
    else:
        running_total = numbers[0]
        for i in range(1, len(numbers)):
            running_total /= numbers[i]
        return round(running_total,2)
    pass


def create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
       
    parser = argparse.ArgumentParser('A simple calculator')
    parser.add_argument('-a','--add', type=float, nargs='+')
    parser.add_argument('-s','--sub', type=float, nargs='+')
    parser.add_argument('-m','--mul', type=float, nargs='+')
    parser.add_argument('-d','--div', type=float, nargs='+')
    
    return parser
    pass


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    call_calculator(stdout=True)