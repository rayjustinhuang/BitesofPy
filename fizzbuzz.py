def fizzbuzz(num):
    
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else: return num
    pass