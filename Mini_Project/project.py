def calculate_average(marks):
    return sum(marks) / len(marks)


def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


print("Student Grade Analyzer")
print("-" * 25)

name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

average = calculate_average(marks)
grade = get_grade(average)

print("\nResult")
print("-" * 25)
print("Student:", name)
print("Total Marks:", sum(marks))
print("Average:", round(average, 2))
print("Grade:", grade)
