class HighScores(object):

	def __init__(self, scores):
		self.scores = scores

	@property
	def scores(self):
		return self._scores

	@scores.setter
	def scores(self, value):
		self._scores = value
		self._sorted_scores = sorted(value, reverse=True)

	def latest(self):
		return self._scores[-1]

	def personal_best(self):
		return self._sorted_scores[0]

	def personal_top_three(self):
		return self._sorted_scores[0:3]

