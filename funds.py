IMPOSSIBLE = 'Mission impossible. No one can contribute.'


def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending
    
    running_total = 0
    max_total = 0
    
    max_start = 0
    max_end = 0
    
    for i in range(len(village)+1):
        for j in range(i, len(village)+1):
            running_total = sum(village[i:j])
            if running_total > max_total:
                max_total = running_total
                max_start = i + 1
                max_end = j
                
                
    return (max_total, max_start, max_end)
    pass