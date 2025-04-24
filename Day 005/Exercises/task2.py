student_scores = [180, 124, 165, 163, 189, 146]

total_exam_score = sum(student_scores)

# sum = 0
# for score in student_scores:
#     sum += score
# print(total_exam_score)
# print(sum)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
