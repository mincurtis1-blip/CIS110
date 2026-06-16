import os
import sys
import termios
import tty

FILE_NAME = "student_grades.txt"
FIELD_NAMES = ["name", "id", "test1", "test2", "test3", "average", "grade"]


def read_single_char(prompt):
    """Read a single character from stdin without requiring Enter."""
    if not sys.stdin.isatty():
        return input(prompt).strip()
    sys.stdout.write(prompt)
    sys.stdout.flush()
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    sys.stdout.write("\n")
    return char


def calculate_average(test1, test2, test3):
    return round((test1 + test2 + test3) / 3, 2)


def calculate_grade(average):
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def load_records():
    students = []
    if not os.path.exists(FILE_NAME):
        return students

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) != len(FIELD_NAMES):
                    print(f"Skipping invalid record line: {line}")
                    continue
                try:
                    student = {
                        "name": parts[0],
                        "id": parts[1],
                        "test1": float(parts[2]),
                        "test2": float(parts[3]),
                        "test3": float(parts[4]),
                        "average": float(parts[5]),
                        "grade": parts[6],
                    }
                except ValueError:
                    print(f"Skipping malformed record line: {line}")
                    continue
                students.append(student)
    except OSError as error:
        print(f"Unable to load records from '{FILE_NAME}': {error}")
    return students


def save_records(students):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for student in students:
                row = (
                    f"{student['name']}|{student['id']}|{student['test1']:.2f}|{student['test2']:.2f}|"
                    f"{student['test3']:.2f}|{student['average']:.2f}|{student['grade']}\n"
                )
                file.write(row)
    except OSError as error:
        print(f"Error saving records to '{FILE_NAME}': {error}")


def display_students(students):
    if not students:
        print("No student records available.")
        return

    header = f"{'Name':<20} | {'ID':<12} | {'Test1':>7} | {'Test2':>7} | {'Test3':>7} | {'Avg':>7} | {'Grade':>5}"
    print(header)
    print("-" * len(header))
    for s in students:
        print(
            f"{s['name']:<20} | {s['id']:<12} | {s['test1']:>7.2f} | {s['test2']:>7.2f} | {s['test3']:>7.2f} | "
            f"{s['average']:>7.2f} | {s['grade']:>5}"
        )


def add_student(students):
    name = input("Enter student name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return False

    student_id = input("Enter student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return False

    test1 = prompt_float("Enter Test 1 score: ")
    if test1 is None:
        print("Add student canceled.")
        return False

    test2 = prompt_float("Enter Test 2 score: ")
    if test2 is None:
        print("Add student canceled.")
        return False

    test3 = prompt_float("Enter Test 3 score: ")
    if test3 is None:
        print("Add student canceled.")
        return False

    average = calculate_average(test1, test2, test3)
    grade = calculate_grade(average)
    student = {
        "name": name,
        "id": student_id,
        "test1": test1,
        "test2": test2,
        "test3": test3,
        "average": average,
        "grade": grade,
    }
    students.append(student)
    print(f"Student record for {name} added. Average: {average:.2f}, Grade: {grade}")
    return True


def add_students(students):
    while True:
        added = add_student(students)
        if added:
            save_records(students)
        choice = input("Would you like to add another student? (Y/N): ").strip().lower()
        if choice != "y":
            break


def class_statistics(students):
    if not students:
        print("No students to calculate statistics.")
        return

    averages = [s["average"] for s in students]
    highest = max(averages)
    lowest = min(averages)
    class_avg = round(sum(averages) / len(averages), 2)
    print(f"Highest average: {highest:.2f}")
    print(f"Lowest average: {lowest:.2f}")
    print(f"Class average:   {class_avg:.2f}")


def search_student(students):
    query = input("Enter student name to search (case-insensitive): ").strip().lower()
    if not query:
        print("Search term cannot be empty.")
        return
    matches = [s for s in students if query in s["name"].lower()]
    if not matches:
        print("Student not found.")
        return
    display_students(matches)


def prompt_float(prompt_text):
    while True:
        raw = input(prompt_text).strip()
        if raw.upper() == "ESC":
            return None
        try:
            value = float(raw)
            if value < 0 or value > 100:
                print("Score must be between 0 and 100.")
                continue
            return value
        except ValueError:
            print("Invalid number. Please enter a valid score or type ESC to cancel.")


def print_menu():
    print("\nStudent Grade Calculator")
    print("1. Add new student record")
    print("2. Display all student records")
    print("3. Show class statistics")
    print("4. Search student by name")
    print("ESC. Exit program")


def main():
    students = load_records()
    print(f"Loaded {len(students)} student record(s) from '{FILE_NAME}'.")

    while True:
        print_menu()
        choice = read_single_char("Choose an option (1-4 or ESC): ")
        if choice == "\x1b" or choice.upper() == "ESC":
            print("Exiting program. Saving student records...")
            save_records(students)
            break
        print()  # newline after menu input
        if choice == "1":
            add_students(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            class_statistics(students)
        elif choice == "4":
            search_student(students)
        else:
            print("Invalid option. Please choose 1-4 or press ESC.")


if __name__ == "__main__":
    main()
