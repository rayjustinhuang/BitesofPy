def sum_numbers(numbers=None):
    if numbers==None:
        return 101*50
    else:
        num_list = list(numbers)
        total = 0
        for i in range(len(num_list)):
            total += num_list[i]
        return total
    pass