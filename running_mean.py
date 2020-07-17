import itertools

def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
       
    for i,j in enumerate(itertools.accumulate(sequence)):
        yield round(j/(i+1),2)
    pass