
# Examination Question Difficulty and Performance Analysis

answer_key = ["A", "B", "C", "D", "A"]

students = ["Student 1", "Student 2",
            "Student 3", "Student 4", "Student 5"]

student_answers = []

total_questions = len(answer_key)
total_students = len(students)

# Accept answers from students
for student in students:

    answers = []

    print("\nEnter answers for", student)

    for i in range(total_questions):

        while True:
            answer = input("Question " + str(i + 1) +
                           " (A/B/C/D): ").upper().strip()

            if answer in ["A", "B", "C", "D", ""]:
                answers.append(answer)
                break
            else:
                print("Invalid answer! Enter A, B, C, D or blank.")

    student_answers.append(answers)

# Initialize question-wise correct counts
correct_counts = [0] * total_questions

print("\n====== STUDENT SCORE REPORT ======")

# Compare student answers with answer key
for i in range(total_students):

    score = 0

    for j in range(total_questions):

        if student_answers[i][j] == answer_key[j]:
            score = score + 1
            correct_counts[j] = correct_counts[j] + 1

    print(students[i], "Score:", score,
          "/", total_questions)

# Question-wise performance analysis
print("\n====== QUESTION ANALYSIS ======")

missed_counts = []

for i in range(total_questions):

    correct = correct_counts[i]
    missed = total_students - correct

    success_rate = (correct / total_students) * 100

    missed_counts.append(missed)

    if success_rate >= 80:
        difficulty = "EASY"

    elif success_rate >= 50:
        difficulty = "MODERATE"

    else:
        difficulty = "DIFFICULT"

    print("\nQuestion:", i + 1)
    print("Correct Answers:", correct)
    print("Missed Answers:", missed)
    print("Success Rate:", round(success_rate, 2), "%")
    print("Difficulty:", difficulty)

# Identify most frequently missed questions
maximum_missed = max(missed_counts)

print("\n====== FINAL ANALYSIS ======")

print("Most Frequently Missed Questions:")

for i in range(total_questions):

    if missed_counts[i] == maximum_missed:
        print("Question", i + 1,
              "- Missed by", maximum_missed, "students")

print("\nAnswer Key:", answer_key)

print("\nExamination Analysis Completed.")
