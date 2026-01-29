# ---------------- AUTHENTICATION SECTION ----------------

users = {}

def signup():
    username = input("Create Username: ")

    if username in users:
        print("User already exists")
        return

    password = input("Create Password: ")

    if len(password) < 4:
        print("Password must be at least 4 characters")
        return

    users[username] = password
    print("Signup Successful")


def login():
    attempts = 3

    while attempts > 0:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username in users and users[username] == password:
            print("Login Successful")
            return True
        else:
            attempts -= 1
            print("Wrong credentials. Attempts left:", attempts)

    print("Account Locked")
    return False


# Authentication Menu
while True:
    print("\n1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        signup()
    elif choice == "2":
        if login():
            break   # Proceed to Fee Management ONLY after successful login
    elif choice == "3":
        print("Thank You")
        exit()
    else:
        print("Invalid choice")


# ---------------- FEE MANAGEMENT SYSTEM ----------------

students = []

while True:
    print("\n--- AcademicFeeManager : College Fee Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Pay Fee")
    print("4. Check Pending Fee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == '1':
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        totalfee = float(input("Enter Total Fee: "))
        paidfee = float(input("Enter Paid Fee: "))

        student = {
            "id": sid,
            "name": name,
            "totalfee": totalfee,
            "paidfee": paidfee
        }

        students.append(student)
        print("Student added successfully!")

    # View All Students
    elif choice == '2':
        if not students:
            print("No student records found.")
        else:
            for s in students:
                pending = s["totalfee"] - s["paidfee"]
                status = "Paid" if pending == 0 else "Pending"

                print("\nID:", s["id"])
                print("Name:", s["name"])
                print("Total Fee:", s["totalfee"])
                print("Paid Fee:", s["paidfee"])
                print("Pending Fee:", pending)
                print("Status:", status)

    # Pay Fee
    elif choice == '3':
        sid = input("Enter Student ID to pay fee: ")
        found = False

        for s in students:
            if s["id"] == sid:
                amount = float(input("Enter amount to pay: "))

                if s["paidfee"] + amount > s["totalfee"]:
                    print("Payment exceeds total fee!")
                else:
                    s["paidfee"] += amount
                    print("Fee paid successfully!")

                found = True
                break

        if not found:
            print("Student not found.")

    # Check Pending Fee
    elif choice == '4':
        sid = input("Enter Student ID: ")
        found = False

        for s in students:
            if s["id"] == sid:
                pending = s["totalfee"] - s["paidfee"]
                print("Pending Fee:", pending)
                found = True
                break

        if not found:
            print("Student not found.")

    # Exit
    elif choice == '5':
        print("Thank you for using AcademicFeeManager!")
        break

    else:
        print("Invalid choice! Please try again.")
