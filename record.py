class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self, score=float('-inf')):
        self.score = score
        
    def __call__(self, score):
        self.score = max(score, self.score)
        return self.score
    pass