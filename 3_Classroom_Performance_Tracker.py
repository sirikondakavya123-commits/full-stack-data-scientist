'''3. Classroom Performance Tracker
Scenario:A teacher wants to track student performance. Write a program to calculate
 the **average marks** of students and identify the **top performer**.
Requirements:
- Use a function to calculate the average marks.
- Identify the student with the highest average.
- Optional: Implement a `Student` class to handle this logic.
Input Example:
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
Expected Output:
Average Marks: {"John": 85, "Alice": 87.33, "Bob": 75}
Top Performer: "Alice"'''
n = int(input("Enter number of students: "))
students = {}
for _ in range(n):
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks (space separated): ").split()))
    students[name] = round(sum(marks) / len(marks), 2)
print("\nAverage Marks:", students)
top_student = max(students, key=students.get)
print("Top Performer:", top_student, "with", students[top_student])
