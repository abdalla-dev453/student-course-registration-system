from models.person import Person
import json


class Student(Person):

    """Student inherits from person"""
    def __init__(self, name, email, student_id, phone_number):
        super().__init__(name, email, phone_number)
        self.student_id = student_id

    
    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "student_id": self.student_id,
            "phone_number": self.phone_number
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"], 
            data["email"], 
            data["student_id"], 
            data["phone_number"]
            )
    
    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Student ID: {self.student_id}\n"
            f"Phone Number: {self.phone_number}\n"
        )