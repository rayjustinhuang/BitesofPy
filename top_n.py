from datetime import datetime
import heapq

numbers = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6]
dates = [datetime(2018, 1, 23, 0, 0),
         datetime(2017, 12, 19, 0, 0),
         datetime(2017, 10, 15, 0, 0),
         datetime(2019, 2, 27, 0, 0),
         datetime(2017, 3, 29, 0, 0),
         datetime(2018, 8, 11, 0, 0),
         datetime(2018, 5, 3, 0, 0),
         datetime(2018, 12, 19, 0, 0),
         datetime(2018, 11, 19, 0, 0),
         datetime(2017, 7, 7, 0, 0)]
# static (outdated) copy of: 
# https://www.forbes.com/celebrities/list
earnings_mln = [
    {'name': 'Kevin Durant', 'earnings': 60.6},
    {'name': 'Adele', 'earnings': 69},
    {'name': 'Lionel Messi', 'earnings': 80},
    {'name': 'J.K. Rowling', 'earnings': 95},
    {'name': 'Elton John', 'earnings': 60},
    {'name': 'Chris Rock', 'earnings': 57},
    {'name': 'Justin Bieber', 'earnings': 83.5},
    {'name': 'Cristiano Ronaldo', 'earnings': 93},
    {'name': 'Beyoncé Knowles', 'earnings': 105},
    {'name': 'Jackie Chan', 'earnings': 49},
]


def get_largest_number(numbers, n=3):
    heapq.heapify(numbers)
    return heapq.nlargest(n, numbers)
    pass


def get_latest_dates(dates, n=3):
    heapq.heapify(dates)
    return heapq.nlargest(n, dates)
    pass


def get_highest_earnings(earnings_mln, n=3):
    heap_master = []
    for x in earnings_mln:
        heap_list = list(x.items())
        heap_entries = (heap_list[1][1], heap_list[0][1])
        heap_master.append(heap_entries)

    heapq.heapify(heap_master)

    final_heap = heapq.nlargest(n, heap_master)
    print(final_heap)
    
    final_list = []
    
    for x in final_heap:
        final_dict = {}
        final_dict['name'], final_dict['earnings'] = x[1], x[0]
        final_list.append(final_dict)
        
    return final_list
    pass