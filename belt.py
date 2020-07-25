import collections

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = zip(scores, belts)

belt_dict = collections.OrderedDict(HONORS)
    
def get_belt(user_score):
        
    if user_score < min(belt_dict.keys()):
        return None
        
    for score, belt in reversed(list(belt_dict.items())):
        if user_score >= score:
            return belt
        else:
            continue
    pass