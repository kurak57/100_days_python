import random
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

students_scores = {name:random.randint(1,100) for name in names}
passed_students = {name:score for (name, score) in students_scores.items() if score >= 60}

print(students_scores)
print(passed_students)