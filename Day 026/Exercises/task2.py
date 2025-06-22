import random as rd

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

rand_scores = {name:rd.randint(0,100) for name in names}
print(rand_scores)

passed_students = {student:score for (student, score) in rand_scores.items() if score >= 60}
print(passed_students)