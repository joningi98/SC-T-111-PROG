class Student(object):
    def __init__(self, score_param=10):
        self.score = score_param

    def add_score(self):
        self.score += 10

    def decrease_score(self):
        self.score -= 10

    def __str__(self):
        return str(self.score)
