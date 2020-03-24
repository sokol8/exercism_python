from high_scores import HighScores

print('hello world')

scores = [30, 50, 20, 70]
expected = [30, 50, 20, 70]

highScores = HighScores(scores)

print(highScores.latest())
