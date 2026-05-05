def get_student_details():
    print("=" * 40)
    print("   STUDENT GRADE CALCULATOR   ")
    print("=" * 40)

    name = input("Enter student name: ")
    num_subjects = int(input("How many subjects? "))

    subjects = {}
    for i in range(num_subjects):
        subject = input(f"Enter subject {i+1} name: ")
        marks = float(input(f"Enter marks for {subject} (out of 100): "))
        subjects[subject] = marks

    return name, subjects

def update_marks(subjects):
    while True:
        print("\n" + "=" * 40)
        print("              CURRENT MARKS" )
        print("="  * 40)
        for subject,marks in subjects.items():
            print(f"{subject:<20} :{marks}/100")
        print("=" * 40)

        update=input("\n Do you want to upadte any marks?(yes/no):")
        if update.lower()=="yes":
            subject_name=input("Enter subject name to update:")

            if subject_name in subjects:
                new_marks=float(input(f"Enter new marksfor {subject_name}:"))
                if 0<=new_marks<=100:
                    subjects[subject_name]=new_marks
                    print(f"\n Marks updated successfullyfor {subject_name}!")
                else:
                    print("\n Invalid Marks!Please enter between 0 and 100.")       
            else:
                print(f"\n Subject '{subject_name}'not found!") 
        elif update.lower()=="no":
            break
        else:
            print("\n Invalid choice! Please enter yes or no.")

    return subjects                        

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


def calculate_rank(percentage):
    if percentage >= 75:
        return "Distinction"
    elif percentage >= 60:
        return "First Class"
    elif percentage >= 50:
        return "Second Class"
    elif percentage >= 40:
        return "Pass Class"
    else:
        return "Fail"


def calculate_results(name, subjects):
    total_marks = sum(subjects.values())
    num_subjects = len(subjects)
    percentage = (total_marks / (num_subjects * 100)) * 100
    grade = calculate_grade(percentage)
    rank = calculate_rank(percentage)

    subject_status = {}
    for subject, marks in subjects.items():
        if marks >= 40:
            subject_status[subject] = "Pass"
        else:
            subject_status[subject] = "Fail"

    overall_status = "Pass" if all(marks >= 40 for marks in subjects.values()) else "Fail"

    return {
        "name": name,
        "subjects": subjects,
        "subject_status": subject_status,
        "total": total_marks,
        "percentage": round(percentage, 2),
        "grade": grade,
        "rank": rank,
        "overall_status": overall_status
    }


def display_results(result):
    print("\n" + "=" * 40)
    print("           RESULT CARD")
    print("=" * 40)
    print(f"Student Name: {result['name']}")
    print("-" * 40)

    for subject, marks in result['subjects'].items():
        status = result['subject_status'][subject]
        print(f"{subject:<20} : {marks:>5} / 100  [{status}]")

    print("-" * 40)
    print(f"Total Marks : {result['total']} / {len(result['subjects']) * 100}")
    print(f"Percentage  : {result['percentage']}%")
    print(f"Grade       : {result['grade']}")
    print(f"Rank        : {result['rank']}")
    print(f"Status      : {result['overall_status']}")
    print("=" * 40)


def save_result(result):
    filename = f"{result['name']}_result.txt"

    with open(filename, "w") as f:
        f.write("=" * 40 + "\n")
        f.write("           RESULT CARD\n")
        f.write("=" * 40 + "\n")
        f.write(f"Student Name: {result['name']}\n")
        f.write("-" * 40 + "\n")

        for subject, marks in result['subjects'].items():
            status = result['subject_status'][subject]
            f.write(f"{subject:<20} : {marks} / 100  [{status}]\n")

        f.write("-" * 40 + "\n")
        f.write(f"Total Marks : {result['total']} / {len(result['subjects']) * 100}\n")
        f.write(f"Percentage  : {result['percentage']}%\n")
        f.write(f"Grade       : {result['grade']}\n")
        f.write(f"Rank        : {result['rank']}\n")
        f.write(f"Status      : {result['overall_status']}\n")
        f.write("=" * 40)

    print(f"\nResult saved to '{filename}' successfully!")


def main():
    while True:
        print("=" * 40)
        print("            MAIN MENU")
        print("=" * 40)
        print("1. Calculate Grade")
        print("2. Exit")
        print("=" * 40)

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            name, subjects = get_student_details()
            subjects=update_marks(subjects)
            result = calculate_results(name, subjects)
            display_results(result)

            save = input("\nDo you want to save the result? (yes/no): ")
            if save.lower() == "yes":
                save_result(result)
        elif choice == "2":
            print("\nThank You! Goodbye!")
            break

        else:
            print("\nInvalid choice! Please enter 1 or 2.")


main()