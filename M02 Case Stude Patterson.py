# Luke Patterson
# M02 Case Study
# Enter a students name and GPA, the program tells if the student has made the dean's list or honor roll

while True:
    last_name = input("Please enter your last name (Enter ZZZ to quit): ")
    if last_name == 'ZZZ':
        break

    first_name = input("Please enter your first name: ")
    gpa = float(input("Please input your GPA: "))

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the dean's list")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the honor role")
    else:
        print(f"{first_name} {last_name} does not qualify for the dean's list or honor role")