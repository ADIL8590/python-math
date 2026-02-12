# write a programme for declaring the results of students with 5 papers and print the result of the students by user input(students) asking them to enter their roll number or name.
def students_list( Name, Roll_Number,School="GHSS SOGAM" , Class="11th", **Marks):
    return {
        "school": School,
        "name": Name,
        "roll_number": Roll_Number,
        "class": Class,
        "marks": {subject: int(mark) for subject, mark in Marks.items()}
    }
students = [
    students_list("Alice", 101, Math=85, English=90, Science=78, History=88, Geography=92),
    students_list("Bob", 102, Math=75, English=80, Science=70, History=65, Geography=72),
    students_list("Charlie", 103, Math=95, English=92, Science=88, History=90, Geography=94),
    students_list("David", 104, Math=60, English=65, Science=55, History=58, Geography=62),
    students_list("Eve", 105, Math=82, English=88, Science=80, History=85, Geography=90),
    students_list("Frank", 106, Math=45, English=50, Science=40, History=42, Geography=48),
    students_list("Grace", 107, Math=70, English=75, Science=65, History=68, Geography=72),
    students_list("Henry", 108, Math=55, English=60, Science=50, History=52, Geography=58),
    students_list("jacky", 109, Math=95, English=60, Science=60, History=58, Geography=68),
    students_list("Henry", 110, Math=65, English=60, Science=70, History=59, Geography=78),
    students_list("Henry", 111, Math=85, English=60, Science=80, History=55, Geography=88),


]

def print_student_result(student):
    total_marks = sum(int(mark) for mark in student["marks"].values())
    average_marks = total_marks / len(student["marks"])
    print(f"School Name:{student["school"]}")
    print(f"Student: {student["name"]}")
    print (f"Roll Number :{student["roll_number"]}")
    print(f"Class: {student ['class']}")
    print(f"Marks: {student['marks']}")
    print(f"Total Marks: {total_marks} out of {len(student['marks']) * 100}")
    print(f"Marks Percentage: {average_marks:.2f}%")
    if average_marks >= 90:
        print("Result: Passed with Distinction")
    elif average_marks >= 60 and average_marks < 90:
        print("Result: Passed with First Class")
    elif average_marks >= 50 and average_marks < 60:
        print("Result: Passed with Second Class")
    elif average_marks >= 40 and average_marks < 50:
        print("Result: Passed with Third Class")
    else:
        print("Result: Failed")
    print("-" * 40)

def find_student_by_roll(roll_number):
    for student in students:
        if student["roll_number"] == roll_number:
            return student
    return None


#if there are multiple students with the same name, we can return a list of students instead of just one. Here's an updated version of the find_student_by_name function:
def find_student_by_name(name):
    matching_students = []
    for student in students:
        if student["name"].lower() == name.lower():
            matching_students.append(student)
    return matching_students if matching_students else None
#Now, if there are multiple students with the same name, the function will return a list of matching students. If no students are found, it will return None.
def print_students_results(students):
    for student in students:
        print_student_result(student)


     



# Get user input
user_input = input("Enter your roll number or name: ")

# Try to find the student by roll number first
student = find_student_by_roll(int(user_input)) if user_input.isdigit() else find_student_by_name(user_input)

if student:
    if isinstance(student, list):
        print_students_results(student)
    else:
        print_student_result(student)
else:
    print("Student not found.")

