class Person:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Phone Number: {self.phone_number}\n"
        )
    