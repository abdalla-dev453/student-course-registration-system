import json

class Course:
    def __init__(self, course_id, course_name, trainer_name, capacity):
        self.course_id = course_id
        self.course_name = course_name
        self.trainer_name = trainer_name
        self.capacity = int(capacity)

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "trainer_name": self.trainer_name,
            "capacity": self.capacity
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["course_id"],
            data["course_name"],
            data["trainer_name"],
            data["capacity"]
        )
    
    def __str__(self):
        return (
            f"Course ID: {self.course_id}\n"
            f"Course Name: {self.course_name}\n"
            f"Trainer Name: {self.trainer_name}\n"
            f"Capacity: {self.capacity}\n"
        )