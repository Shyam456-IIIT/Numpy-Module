# Student Grade Analyzer: Build a small system that processes exam scores using pure Numpy
import numpy as np

np.random.seed(42)
scores=np.random.randint(30,101,(20,5))
subjects=['Maths','Physics','Chemistry','Biology','Telugu']
print(scores)

print("------")
print("The Average of all the students:")
print(scores.mean(axis=1).reshape(20,1))

print("------")

print("Each Subject average:")
print(subjects)
print(scores.mean(axis=0))

print("The Top scorers in each subject:")
print(scores.max(axis=0))
print(scores.argmax(axis=0))

print("------")
print("Topper of the Class (ID): ",scores.mean(axis=1).argmax())
print("Topper of the Class (SCORED): ",scores.mean(axis=1).max())
print("Topper of the Class (SCORES): ",scores[scores.mean(axis=1).argmax()])

print("Failed Students:")
print((scores < 40).any(axis=1))
print(scores[(scores < 40).any(axis=1)])

normalize=(scores - scores.min())/(scores.max() - scores.min())
print(normalize)

print("-------")
bonus_scores=scores+5
final_scores=np.clip(bonus_scores,min=None,max=100)
print(final_scores)






