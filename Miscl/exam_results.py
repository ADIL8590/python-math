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
    students_list("Alice", 101, Math=85, English=90, Physics=78, Chemistry=88, Biology=92),
    students_list("Bob", 102, Math=75, English=80, Physics=70, Chemistry=65, Biology=72),
    students_list("Charlie", 103, Math=95, English=92, Physics=88, Chemistry=90, Biology=94),
    students_list("David", 104, Math=60, English=65, Physics=55, Chemistry=58, Biology=62),
    students_list("Eve", 105, Math=82, English=88, Physics=80, Chemistry=85, Biology=90),
    students_list("Frank", 106, Math=45, English=50, Physics=40, Chemistry=42, Biology=48),
    students_list("Grace", 107, Math=70, English=75, Physics=65, Chemistry=68, Biology=72),
    students_list("Henry", 108, Math=55, English=60, Physics=50, Chemistry=52, Biology=58),
    students_list("jacky", 109, Math=95, English=60, Physics=60, Chemistry=58, Biology=68),
    students_list("Henry", 110, Math=65, English=60, Physics=70, Chemistry=59, Biology=78),
    students_list("Henry", 111, Math=85, English=60, Physics=80, Chemistry=55, Biology=88),
    students_list("Henry", 112, Math=85, English=60, Science=80, History=55, Geography=88),
    students_list("Henry", 113, Math=85, English=60, Science=80, History=55, Geography=88),
    students_list("Mogli", 114, Math=45, English=30, Science=40, History=35, Geography=28),
    students_list("Mooz", 115, Math=25, English=30, Science=39, History=35, Geography=28),


]

def print_student_result(student):
    failed_subjects = [subject for subject, mark in student['marks'].items() if int(mark) < 40]
    total_marks = sum(int(mark) for mark in student["marks"].values())
    average_marks = total_marks / len(student["marks"])
    print(f"School Name:{student['school']}")
    print(f"Student: {student['name']}")
    print (f"Roll Number :{student['roll_number']}")
    print(f"Class: {student ['class']}")
    
    if len(failed_subjects) >= 1 and len(failed_subjects) < 5:
        print("Overall Result: Re-appear")
        print(f"Failed Subjects: {', '.join(failed_subjects)} with marks: {', '.join(str(student['marks'][subject]) for subject in failed_subjects)} respectively")
        return
        
    elif len(failed_subjects) == 5:
        print("Overall Result: Failed")
        print(f"Failed Subjects: {', '.join(failed_subjects)} with marks: {', '.join(str(student['marks'][subject]) for subject in failed_subjects)} respectively")
        return
    else:
       print("Subject-wise Results:")
    for subject, mark in student['marks'].items():
            if int(mark) >= 40:
                print(f"  {subject}:  ({mark})     Passed")
            else:
                print(f"  {subject}:  ({mark})     Failed")

    #print(f"Marks:{student['marks']}")     Note: alternative to print subject-wise results
    print(f"Total Marks Obetained : {total_marks} out of {len(student['marks']) * 100}")
    print(f"Marks Percentage: {average_marks:.2f}%")
    # add grading system
     
    if average_marks >= 90:
            print("Result: Passed with Distinction")
    elif average_marks >= 60 and average_marks < 90:
            print("Result: Passed with First Class")
    elif average_marks >= 50 and average_marks < 60:
          print("Result: Passed with Second Class")
    else:
         print("Result: Passed with Third Class")
         
        
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

