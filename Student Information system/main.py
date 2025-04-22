import csv
import os
import statistics
import matplotlib.pyplot as plt

CSV_FILE = "student_marks.csv"

def load_data():
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_data(data):
    with open(CSV_FILE, 'w', newline='') as file:
        fieldnames = ["StudentID", "Name", "Math", "Science", "English"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def add_student():
    data = load_data()
    student = {
        "StudentID": input("Enter ID: "),
        "Name": input("Enter Name: "),
        "Math": input("Enter Math Marks: "),
        "Science": input("Enter Science Marks: "),
        "English": input("Enter English Marks: ")
    }
    data.append(student)
    save_data(data)
    print("Student added.")

def update_student():
    data = load_data()
    sid = input("Enter student ID to update: ")
    for student in data:
        if student["StudentID"] == sid:
            student["Name"] = input("Enter new Name: ")
            student["Math"] = input("Enter new Math Marks: ")
            student["Science"] = input("Enter new Science Marks: ")
            student["English"] = input("Enter new English Marks: ")
            save_data(data)
            print("Student updated.")
            return
    print("Student not found.")

def delete_student():
    data = load_data()
    sid = input("Enter student ID to delete: ")
    new_data = [s for s in data if s["StudentID"] != sid]
    save_data(new_data)
    print("Student deleted.")

def calculate_gpa(marks):
    marks = list(map(int, marks))
    return round(sum(marks) / len(marks) / 25, 2)  # GPA out of 4.0

def view_summary():
    data = load_data()
    for s in data:
        marks = [int(s["Math"]), int(s["Science"]), int(s["English"])]
        gpa = calculate_gpa(marks)
        print(f"{s['Name']} (ID: {s['StudentID']}) - GPA: {gpa}")

def find_topper():
    data = load_data()
    top_student = max(data, key=lambda s: sum(map(int, [s["Math"], s["Science"], s["English"]])))
    print(f"Topper: {top_student['Name']} (ID: {top_student['StudentID']})")

def visualize_data():
    data = load_data()
    names = [s["Name"] for s in data]
    math = [int(s["Math"]) for s in data]
    science = [int(s["Science"]) for s in data]
    english = [int(s["English"]) for s in data]

    x = range(len(names))
    plt.bar(x, math, label='Math')
    plt.bar(x, science, bottom=math, label='Science')
    plt.bar(x, english, bottom=[math[i]+science[i] for i in x], label='English')

    plt.xticks(x, names, rotation=45)
    plt.ylabel('Marks')
    plt.title('Student Marks Comparison')
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("\nStudent Information System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View GPA Summary")
        print("5. Find Topper")
        print("6. Visualize Data")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            view_summary()
        elif choice == "5":
            find_topper()
        elif choice == "6":
            visualize_data()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
