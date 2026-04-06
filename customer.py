from db import get_connection

def customer():
    print("\n------ CUSTOMER MENU ------")
    print("1. Add Customer")
    print("2. Modify Customer")
    print("3. Delete Customer")
    print("4. Display Customer")
    print("5. Back")

    choice = input("Enter choice: ")

    if choice == '1':
        addcustomer()
    elif choice == '2':
        modcust()
    elif choice == '3':
        delcust()
    elif choice == '4':
        discust()
    else:
        return
def addcustomer():
    con = get_connection()
    if not con:
        print(" Database connection failed")
        return

    cur = con.cursor()

    try:
        Id = input("Enter Customer Id (6 digits): ")
        if len(Id) != 6:
            print("Invalid ID")
            return

        cur.execute("SELECT * FROM customer WHERE c_id=%s", (Id,))
        if cur.fetchone():
            print("ID already exists")
            return

        Name = input("Enter Name: ")
        Contact = input("Enter Contact (10 digits): ")
        if len(Contact) != 10:
            print("Invalid Contact")
            return

        Address = input("Enter Address: ")
        Passport = input("Enter Passport (7 digits): ")
        if len(Passport) != 7:
            print("Invalid Passport")
            return

        Age = input("Enter Age: ")

        cur.execute(
            "INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s)",
            (Id, Name, Contact, Address, Passport, Age)
        )

        con.commit()
        print("Customer Added")

    except Exception as e:
        print("Error:", e)

    finally:
        con.close()


def modcust():
    con = get_connection()
    if not con:
        print(" Connection failed")
        return

    cur = con.cursor()

    Id = input("Enter Customer ID: ")
    cur.execute("SELECT * FROM customer WHERE c_id=%s", (Id,))
    if not cur.fetchone():
        print("Customer not found")
        return

    print("1. Change Name")
    print("2. Change Contact")
    print("3. Change Passport")

    ch = input("Enter choice: ")

    if ch == '1':
        new = input("Enter new name: ")
        cur.execute("UPDATE customer SET name=%s WHERE c_id=%s", (new, Id))

    elif ch == '2':
        new = input("Enter new contact: ")
        if len(new) != 10:
            print("Invalid contact")
            return
        cur.execute("UPDATE customer SET contact=%s WHERE c_id=%s", (new, Id))

    elif ch == '3':
        new = input("Enter new passport: ")
        if len(new) != 7:
            print("Invalid passport")
            return
        cur.execute("UPDATE customer SET passport=%s WHERE c_id=%s", (new, Id))

    else:
        print("Invalid choice")
        return

    con.commit()
    con.close()
    print(" Updated successfully")


def delcust():
    con = get_connection()
    if not con:
        print(" Connection failed")
        return

    cur = con.cursor()

    Id = input("Enter Customer ID to delete: ")

    cur.execute("SELECT * FROM customer WHERE c_id=%s", (Id,))
    if not cur.fetchone():
        print("Customer not found")
        return

    cur.execute("DELETE FROM customer WHERE c_id=%s", (Id,))
    con.commit()
    con.close()

    print(" Customer deleted")



def discust():
    con = get_connection()
    if not con:
        print("❌ Connection failed")
        return

    cur = con.cursor()

    print("1. Show All")
    print("2. Search by ID")

    ch = input("Enter choice: ")

    if ch == '1':
        cur.execute("SELECT * FROM customer")
        data = cur.fetchall()

        if not data:
            print("No records found")
        else:
            for row in data:
                print(row)

    elif ch == '2':
        Id = input("Enter Customer ID: ")
        cur.execute("SELECT * FROM customer WHERE c_id=%s", (Id,))
        row = cur.fetchone()

        if not row:
            print("Customer not found")
        else:
            print(row)

    else:
        print("Invalid choice")

    con.close()

    
