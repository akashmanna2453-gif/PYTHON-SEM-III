def student_info(name, age=18):
    print("Name:", name)
    print("Age:", age)


def calculate_marks(m1, m2, m3):
    total = m1 + m2 + m3
    return total


def check_result(total, passing_marks=40):
    if total >= passing_marks:
        return "PASS"
    else:
        return "FAIL"


def display_result(name, total, result):
    print("\n----- RESULT -----")
    print("Student:", name)
    print("Total Marks:", total)
    print("Result:", result)


# Positional arguments
student_info("Akash", 18)

# Keyword arguments
student_info(age=18, name="Rahul")

# Default argument
student_info("Rohan")

# Calling function and passing arguments
marks = calculate_marks(75, 82, 69)

# Return value stored in variable
result = check_result(marks)

# Passing returned values to another function
display_result("Akash", marks, result)
