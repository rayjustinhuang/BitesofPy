def sum_numbers(numbers=None):
    if numbers==None:
        return 101*50
    else:
        num_list = list(numbers)
        total = 0
        for i in numbers:
            total += num_list[i]
        return total
    pass