import random

student_scores = list()
for i in range(0,20):
    student_scores.append(random.randint(100,200))

print(f"These are the student scores: {student_scores}")

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

student_scores.sort(reverse=True)
min_score = student_scores[-1]

print(f"The highest score in the class is: {max_score}")
print(f"The lowest score in the class is: {min_score}")