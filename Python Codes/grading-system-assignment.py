# School Grading Assignment
# Rewrite this program using your own variable names and output messages
# student name:
# Student number:
# Major:

student_name = input("Enter your full name: ")

student_number = input("Enter your number: ")

student_major = input("Enter your major: ")

course_name = input("Enter your course's name: ")

student_score = float(input("Enter your score: "))


if student_score >= 90:
    print(
        f"Student's name: \t {student_name}\n Student's number: \t {student_number}\nMajor: \t\t\t {student_major}\nCourse name: \t\t {course_name}\nScore: \t\t\t {student_score}\n Grade: \t\t A"
    )
elif student_score >= 80:
    print(
        f"Student's name: \t {student_name}\n Student's number: \t {student_number}\nMajor: \t\t\t {student_major}\nCourse name: \t\t {course_name}\nScore: \t\t\t {student_score}\n Grade: \t\t B"
    )
elif student_score >= 70:
    print(
        f"Student's name: \t {student_name}\n Student's number: \t {student_number}\nMajor: \t\t\t {student_major}\nCourse name: \t\t {course_name}\nScore: \t\t\t {student_score}\n Grade: \t\t C"
    )
elif student_score >= 60:
    print(
        f"Student's name: \t {student_name}\n Student's number: \t {student_number}\nMajor: \t\t\t {student_major}\nCourse name: \t\t {course_name}\nScore: \t\t\t {student_score}\n Grade: \t\t D"
    )
else:
    print(
        f"Student's name: \t {student_name}\n Student's number: \t {student_number}\nMajor: \t\t\t {student_major}\nCourse name: \t\t {course_name}\nScore: \t\t\t {student_score}\n Grade: \t\t F"
    )
