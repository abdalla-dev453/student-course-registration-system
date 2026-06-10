from services.school_system import SchoolSystem


def display_menu():
    print("\n" + "=" * 50)
    print(" STUDENT COURSE REGISTRATION SYSTEM ")
    print("=" * 50)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Add Course")
    print("5. View Courses")
    print("6. Register Student to Course")
    print("7. View Students in a Course")
    print("8. View Courses for a Student")
    print("9. Save Data")
    print("10. Load Data")
    print("0. Exit")
    print("=" * 50)


def main():
    system = SchoolSystem()

    # Automatically load existing data
    system.load_data()

    while True:
        display_menu()

        choice = input("Choose an option: ").strip()

        # ==========================
        # ADD STUDENT
        # ==========================
        if choice == "1":

            print("\nAdd Student")

            student_id = input("Student ID: ").strip()
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            phone = input("Phone Number: ").strip()

            system.add_student(
                student_id,
                name,
                email,
                phone
            )

        # ==========================
        # VIEW STUDENTS
        # ==========================
        elif choice == "2":
            system.view_students()

        # ==========================
        # SEARCH STUDENT
        # ==========================
        elif choice == "3":

            search_term = input(
                "Enter Student ID or Name: "
            ).strip()

            system.search_student(search_term)

        # ==========================
        # ADD COURSE
        # ==========================
        elif choice == "4":

            print("\nAdd Course")

            course_id = input("Course ID: ").strip()

            course_name = input(
                "Course Name: "
            ).strip()

            trainer = input(
                "Trainer Name: "
            ).strip()

            capacity = input(
                "Capacity: "
            ).strip()

            system.add_course(
                course_id,
                course_name,
                trainer,
                capacity
            )

        # ==========================
        # VIEW COURSES
        # ==========================
        elif choice == "5":
            system.view_courses()

        # ==========================
        # REGISTER STUDENT
        # ==========================
        elif choice == "6":

            print("\nRegister Student")

            student_id = input(
                "Student ID: "
            ).strip()

            course_id = input(
                "Course ID: "
            ).strip()

            system.register_student_to_course(
                student_id,
                course_id
            )

        # ==========================
        # VIEW STUDENTS IN COURSE
        # ==========================
        elif choice == "7":

            course_id = input(
                "Course ID: "
            ).strip()

            system.view_students_in_course(
                course_id
            )

        # ==========================
        # VIEW COURSES FOR STUDENT
        # ==========================
        elif choice == "8":

            student_id = input(
                "Student ID: "
            ).strip()

            system.view_courses_for_student(
                student_id
            )

        # ==========================
        # SAVE DATA
        # ==========================
        elif choice == "9":
            system.save_data()

        # ==========================
        # LOAD DATA
        # ==========================
        elif choice == "10":
            system.load_data()

        # ==========================
        # EXIT
        # ==========================
        elif choice == "0":

            print("\nSaving data...")

            system.save_data()

            print(
                "Thank you for using the "
                "Student Course Registration System."
            )

            break

        # ==========================
        # INVALID OPTION
        # ==========================
        else:
            print(
                "Invalid choice. "
                "Please select a valid option."
            )


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

    except Exception as error:
        print(f"\nUnexpected error: {error}")