import numpy as np
import matplotlib.pyplot as plt
input_path = "data/students.csv"
with open(input_path,"r") as file :
    text = file.read()
lines = text.splitlines()
print(lines)
header = lines[0]
print("Header:",header)
columns = header.split(",")
print("Columns:",columns)
students_result = []
class_total = 0
student_count = 0
math_total = 0
english_total = 0
cs_total = 0
for line in lines[1:]:
    parts = line.split(",")
    name = parts[0]
    math = int(parts[1])
    math_total = math_total + math
    english = int(parts[2])
    english_total = english_total + english
    cs = int(parts[3])
    cs_total = cs_total + cs
    total = math + english + cs
    original_average = total / 3
    average = round(original_average,2)
    print(parts)
    print("Total:",total)
    print("Average:",average)
    students_result.append([name, math, english, cs, total, average])
    student_count = student_count + 1
    class_total = class_total + original_average
class_average = round(class_total / student_count,2)
math_average = round(math_total / student_count,2)
english_average = round(english_total / student_count,2)
cs_average = round(cs_total / student_count,2)
print("Class Average:",class_average)
print("Math Average:",math_average)
print("English Average:",english_average)
print("CS Average",cs_average)
best_average = -1
best_student = ""
for student in students_result:
    if student[5] > best_average:
        best_average = student[5]
        best_student = student[0]
print("Best student:",best_student)
print("Best average:",best_average)
output_path = "data/students_output.csv"
with open(output_path,"w") as file:
    file.write("name,math,english,cs,total,average,grade\n")
    for student in students_result :
        grade = ""
        if student[5] >= 90:
            grade = "A"
        elif student[5] >= 80:
            grade = "B"
        elif student[5] >= 70:
            grade = "C"
        else:
            grade = "D"
        file.write(student[0]+","+str(student[1])+","+str(student[2])+","+str(student[3])+","+str(student[4])+","+str(student[5])+","+grade+'\n')
names = [student[0] for student in students_result]
math_scores = [student[1] for student in students_result]
english_scores = [student[2] for student in students_result]
cs_scores = [student[3] for student in students_result]

x = np.arange(len(names)) 
width = 0.25 
fig, ax = plt.subplots(figsize=(12, 6))

rects1 = ax.bar(x - width, math_scores, width, label='Math', color='skyblue')
rects2 = ax.bar(x, english_scores, width, label='English', color='lightgreen')
rects3 = ax.bar(x + width, cs_scores, width, label='CS', color='salmon')

ax.set_xlabel('Students')
ax.set_ylabel('Scores')
ax.set_title('Student Scores by Subject')
ax.set_xticks(x)
ax.set_xticklabels(names, rotation=45, ha='right')
ax.legend()


ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

plt.tight_layout()
plt.savefig("data/student_scores.png", dpi=200)
plt.show()