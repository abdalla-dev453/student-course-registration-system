from models.student import Student
from models.course import Course

student = Student(
    "S001",
    "Mary Wanjiku",
    "mary@example.com",
    "0711111111"
)

course = Course(
    "PY101",
    "Python Fundamentals",
    "Mr. Joseph",
    5
)

print(student)
print("-" * 30)
print(course)