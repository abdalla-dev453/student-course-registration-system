from services.school_system import SchoolSystem

system = SchoolSystem()

# Students
system.add_student(
    "S001",
    "Mary Wanjiku",
    "mary@example.com",
    "0711111111"
)

system.add_student(
    "S002",
    "John Mwangi",
    "john@example.com",
    "0722222222"
)

system.add_student(
    "S003",
    "James Otieno",
    "james@example.com",
    "0733333333"
)

# Course
system.add_course(
    "PY101",
    "Python Fundamentals",
    "Mr. Joseph",
    2
)

# Registrations
system.register_student_to_course(
    "S001",
    "PY101"
)

system.register_student_to_course(
    "S001",
    "PY101"
)

system.register_student_to_course(
    "S002",
    "PY101"
)

system.register_student_to_course(
    "S003",
    "PY101"
)

# Views
system.view_students_in_course("PY101")

system.view_courses_for_student("S001")