s = int(input("Enter number of students: "))
n = int(input("Enter number of subjects: "))

class_total = 0

for i in range(1, s+1):
    print("Student", i)
    student_total = 0
    for j in range(1, n+1):
        score = float(input("Enter score " + str(j) + ": "))
        student_total += score
    avg = student_total / n
    print("Average for Student", i, "=", avg)
    class_total += avg

print("Class Average =", class_total / s)

