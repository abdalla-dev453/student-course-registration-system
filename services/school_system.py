from models.course import Course
from models.student import Student

import json
import os

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

        student = Student(name, email, student_id, phone_number)
        
        self.students[student_id] = student

        print(f"Student {name} added successfully")


    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        
        print("\n======== Students =========")

        for student in self.students.values():
            print(student)

    
    def search_student(self, search_term):
        found = False

        for student in self.students.values():
             
            if (
                student.student_id.lower() == search_term.lower()
                or search_term.lower() in student.name.lower()
            ):
                print(student)
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
        
        print("\n== Courses ==")

        for course in self.courses.values():
            print(course)


# ========================== REGISTRATIONS MANAGEMENT =====================
    def register_student_to_course(self, student_id, course_id):
        # condition to check if student exists
        """Validations"""
        if student_id not in self.students:
            print("Student not found.")
            return

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
    
                found = True
    
        if not found:
            print("No courses found for this student.")
    
    
    # =============File I/O==================Saving data============
    def save_data(self):
    
        os.makedirs("data", exist_ok=True)
    
        # Save students
        students_data = [
            student.to_dict()
            for student in self.students.values()
        ]
    
        with open( "data/students.json", "w" ) as file:
    
            json.dump( students_data, file, indent=4 )
    
        # Save courses
        courses_data = [
            course.to_dict()
            for course in self.courses.values()
        ]
    
        with open( "data/courses.json", "w") as file:
    
            json.dump( courses_data, file, indent=4 )
    
        # Save registrations
        with open(
            "data/registrations.json",
            "w",
            encoding="utf-8"
        ) as file:
    
            json.dump(self.registrations,file,indent=4)
    
        print("Data saved successfully.")
    
    
    # ===============File I/O==================Loading data============
    def load_data(self):
    
        # Students
        try:
            with open(
                "data/students.json",
                "r"
            ) as file:
    
                students_data = json.load(file)
    
                self.students = {
                    item["student_id"]:
                    Student.from_dict(item)
                    for item in students_data
                }
    
        except FileNotFoundError:
            self.students = {}
    
        # Courses
        try:
            with open(
                "data/courses.json",
                "r"
            ) as file:
    
                courses_data = json.load(file)
    
                self.courses = {
                    item["course_id"]:
                    Course.from_dict(item)
                    for item in courses_data
                }
    
        except FileNotFoundError:
            self.courses = {}
    
        # Registrations
        try:
            with open(
                "data/registrations.json",
                "r",
                encoding="utf-8"
            ) as file:
    
                self.registrations = json.load(file)
    
        except FileNotFoundError:
            self.registrations = {}
    
        print("Data loaded successfully.")