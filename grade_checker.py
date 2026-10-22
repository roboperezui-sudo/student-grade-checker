
def get_student_info():
    name = input("Enter student name: ")
    scores = []

    for i in range(3):
        score = float(input(f"Enter score for subject {i + 1}: "))
        scores.append(score)

    return name, scores


def calculate_average(scores):
    return sum(scores) / len(scores)


def display_result(name, average):
    print("\n--- Student Grade Report ---")
    print("Student Name:", name)
    print("Average Grade:", round(average, 2))

    if average >= 75:
        print("Status: PASSED")
    else:
        print("Status: FAILED")


name, scores = get_student_info()
average = calculate_average(scores)
display_result(name, average)

