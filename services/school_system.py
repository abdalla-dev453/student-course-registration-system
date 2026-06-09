from models.course import Course
from models.student import Student

class SchoolSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.registrations = {}
 
# ========================== STUDENTS MANAGEMENT =========================
    def add_student(self, student_id, name, email, phone_number):
        # validation
        if not student_id.strip():
            print("Student ID cannot be empty")
            return
        
        if not name.strip():
            print("Name cannot be empty")
            return
        
        if "@" not in email:
            print("Invalid email format")
            return
        
        if not phone_number.strip():
            print("Phone number cannot be empty")
            return
        
        if student_id in self.students:
            print("Student ID already exists")
            return

        student = Student(name, 
                          email, 
                          student_id, 
                          phone_number)
        
        self.students[student_id] = student

        print(f"Student {name} added successfully")


    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        
        print("\n======== Students =========")

        for student in self.students.values():
            print(student)
            print("-" * 40)

    
    def search_student(self, search_term):
        found = False

        for student in self.students.values():
             
            if (
                student.student_id.lower() == search_term.lower()
                or search_term.lower() in student.name.lower()
            ):
                print(student)
                print("-" * 40)
                found = True

        if not found:
            print("No matching student found.")

# ========================== COURSES MANAGEMENT ===========================


    def add_course(
            self,
            course_id,
            course_name,
            trainer_name,
            capacity    
    ):
        if not course_id.strip():
            print("Course ID cannot be empty")
            return
        
        if not course_name.strip():
            print("Course name cannot be empty")
            return
        
        if not trainer_name.strip():
            print("Trainer name cannot be empty")
            return
        
        try:
            capacity = int(capacity)

            if capacity <= 0:
                print("Capacity must be a positive integer")
                return
            
        except ValueError:
            print("Capacity must be a validi number")
            return
        
        if course_id in self.courses:
            print("Course ID already exists")
            return
        

        course = Course(
            course_id,
            course_name,
            trainer_name,
            capacity
        )

        self.courses[course_id] = course

        print(f"Course {course_name} added successfully")


    def view_courses(self):
        if not self.courses:
             print("No courses found.")
        return
        
        print("\n======== Courses =========")

        for course in self.courses.values():
            print(course)
            print("-" * 40)


# ========================== REGISTRATIONS MANAGEMENT =====================
def register_student_to_course(self, student_id, course_id):
    """Validations"""
    # condition to check if student exists
    if student_id not in self.students:
        print("Student not found.")
        return

    # Condition to check if course exists
    if course_id not in self.courses:
        print("Course not found.")
        return

    # Checking for registration list
    if course_id not in self.registrations:
        self.registrations[course_id] = []

    # Already registered?
    if student_id in self.registrations[course_id]:
        student = self.students[student_id]

        print(
            f"{student.name} is already registered for this course."
        )
        return

    # Capacity check
    course = self.courses[course_id]

    if len(self.registrations[course_id]) >= course.capacity:
        print(
            "Registration failed. This course is already full."
        )
        return

    # Register
    self.registrations[course_id].append(student_id)

    student = self.students[student_id]

    print(
        f"{student.name} successfully registered for "
        f"{course.course_name}."
    )


# View registrations
def view_students_in_course(self, course_id):

    if course_id not in self.courses:
        print("Course not found.")
        return

    course = self.courses[course_id]

    print(f"Students in {course.course_name}:")

    students = self.registrations.get(course_id, [])

    if not students:
        print("No students registered for this course.")
        return
    
    for student_id in students:
        print(self.students[student_id])
        print("-" * 40)

# view course
def view_courses_for_student(self, student_id):

    if student_id not in self.studens:
        print("Student not found.")
        return

    student = self.students[student_id]

    print(f"Courses for {student.name}:")
    
    found = False

    for course_id, student_id in self.registrations.items:
        if student_id == student_id:
            course = self.courses[course_id]
            print(course)
            print("-" * 40)

            found = True

    if not found:
        print("No courses found for this student.")