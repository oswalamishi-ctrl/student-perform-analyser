def student_performance():
    # Collect student details
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")

    # Collect subject marks
    subjects = {}
    num_subjects = int(input("Enter number of subjects: "))
    for i in range(num_subjects):
        subject = input(f"Enter subject {i+1} name: ")
        marks = int(input(f"Enter marks for {subject}: "))
        subjects[subject] = marks

    # Calculations
    total = sum(subjects.values())
    average = total / len(subjects)
    highest_subject = max(subjects, key=subjects.get)
    lowest_subject = min(subjects, key=subjects.get)

    # Display report
    print("\n--- Student Performance Report ---")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print("Subjects and Marks:")
    for subject, marks in subjects.items():
        print(f"  {subject}: {marks}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Scoring Subject: {highest_subject} ({subjects[highest_subject]})")
    print(f"Lowest Scoring Subject: {lowest_subject} ({subjects[lowest_subject]})")


# Run the program
if __name__ == "__main__":
    student_performance()
