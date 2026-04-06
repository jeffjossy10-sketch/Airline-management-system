from db import get_connection


def employee():
    con = get_connection()
    if not con:
        print("Connection failed")
        return

    cur = con.cursor()

    print("\n      EMPLOYEE MENU      ")
    print("-" * 30)
    print("(1) ADD EMPLOYEE")
    print("(2) MODIFY EMPLOYEE")
    print("(3) REMOVE EMPLOYEE")
    print("(4) LIST ALL EMPLOYEE")
    print("(5) SEARCH EMPLOYEE")

    ch = int(input("\nEnter your choice: "))

    # -------- ADD EMPLOYEE --------
    if ch == 1:
        eid = int(input("Enter employee id (3 digits): "))

        if len(str(eid)) != 3:
            print("Employee id should be 3 digits")
            return

        cur.execute("SELECT * FROM emp WHERE empid=%s", (eid,))
        if cur.fetchone():
            print("Id already exists")
            return

        name = input("Enter name: ")
        contact = input("Enter contact number: ")

        if len(contact) != 10:
            print("Contact must be 10 digits")
            return

        gender = input("Enter gender (M/F): ")
        if len(gender) != 1:
            print("Invalid gender")
            return

        address = input("Enter address: ")
        age = input("Enter age: ")

        if len(age) > 3:
            print("Invalid age")
            return

        cur.execute(
            "INSERT INTO emp VALUES (%s, %s, %s, %s, %s, %s)",
            (eid, name, contact, gender, address, age)
        )

        con.commit()
        con.close()
        print("Employee added successfully")

    # -------- MODIFY EMPLOYEE --------
    elif ch == 2:
        print("1. MODIFY NAME")
        print("2. MODIFY CONTACT")
        print("3. MODIFY ADDRESS")
        print("4. MODIFY AGE")

        choice = int(input("Enter your choice: "))
        eid = int(input("Enter employee id: "))

        cur.execute("SELECT * FROM emp WHERE empid=%s", (eid,))
        if not cur.fetchone():
            print("Employee not found")
            return

        if choice == 1:
            new = input("Enter new name: ")
            cur.execute("UPDATE emp SET name=%s WHERE empid=%s", (new, eid))

        elif choice == 2:
            new = input("Enter new contact: ")
            if len(new) != 10:
                print("Invalid contact")
                return
            cur.execute("UPDATE emp SET contact=%s WHERE empid=%s", (new, eid))

        elif choice == 3:
            new = input("Enter new address: ")
            cur.execute("UPDATE emp SET address=%s WHERE empid=%s", (new, eid))

        elif choice == 4:
            new = input("Enter new age: ")
            if len(new) > 3:
                print("Invalid age")
                return
            cur.execute("UPDATE emp SET age=%s WHERE empid=%s", (new, eid))

        else:
            print("Invalid choice")
            return

        con.commit()
        con.close()
        print("Employee updated successfully")

    # -------- DELETE EMPLOYEE --------
    elif ch == 3:
        eid = int(input("Enter employee id to delete: "))

        cur.execute("SELECT * FROM emp WHERE empid=%s", (eid,))
        if not cur.fetchone():
            print("Employee not found")
            return

        cur.execute("DELETE FROM emp WHERE empid=%s", (eid,))
        con.commit()
        con.close()

        print("Employee removed successfully")

    # -------- LIST EMPLOYEES --------
    elif ch == 4:
        cur.execute("SELECT * FROM emp")
        data = cur.fetchall()

        if not data:
            print("No employees found")
        else:
            print("ID   NAME   CONTACT   GENDER   ADDRESS   AGE")
            for row in data:
                print(row)

        con.close()

    # -------- SEARCH EMPLOYEE --------
    elif ch == 5:
        eid = int(input("Enter employee id: "))

        cur.execute("SELECT * FROM emp WHERE empid=%s", (eid,))
        row = cur.fetchone()

        if not row:
            print("Employee not found")
        else:
            print("ID:", row[0])
            print("Name:", row[1])
            print("Contact:", row[2])
            print("Gender:", row[3])
            print("Address:", row[4])
            print("Age:", row[5])

        con.close()

    else:
        print("Invalid choice")
