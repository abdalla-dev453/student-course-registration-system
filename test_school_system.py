from services.school_system import SchoolSystem

system = SchoolSystem()

# Add students
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

# View students
system.view_students()

# Search student
system.search_student("Mary")

# Add course
system.add_course(
    "PY101",
    "Python Fundamentals",
    "Mr. Joseph",
    5
)

# View courses
system.view_courses()