scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        if 10 <= new_score < 50:
            return BELTS[10]
        elif 50 <= new_score < 100:
            return BELTS[50]
        elif 100<= new_score < 175:
            return BELTS[100]
        elif 175 <= new_score < 250:
            return BELTS[175]
        elif 250 <= new_score < 400:
            return BELTS[250]
        elif 400 <= new_score < 600:
            return BELTS[400]
        elif 600 <= new_score < 800:
            return BELTS[600]
        elif 800 <= new_score < 1000:
            return BELTS[800]
        else:
            return BELTS[1000]
            
        pass

    def _get_score(self):
        return self._score
        pass

    def _set_score(self, new_score):
        if new_score <= self._score:
            raise ValueError
        else:
            self._last_earned_belt = map(BELTS, new_score)
            self._score = new_score
        pass

    score = property(_get_score, _set_score)
    
print(BELTS[49])