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