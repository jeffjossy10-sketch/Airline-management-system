from db import get_connection


def flight():
    con = get_connection()
    if not con:
        print("Connection failed")
        return

    cur = con.cursor()

    print("\n      FLIGHT  MENU      ")
    print("-" * 30)
    print("(1) ADD FLIGHT")
    print("(2) MODIFY FLIGHT")
    print("(3) REMOVE FLIGHT")
    print("(4) LIST ALL FLIGHTS")
    print("(5) INDIVIDUAL SEARCH")

    ch = int(input("\nEnter your choice: "))

    # -------- ADD FLIGHT --------
    if ch == 1:
        i = int(input("Enter the flight id: "))
        k = length(i)

        if k != 0:
            print("Id already exists")
            return

        if len(str(i)) != 3:
            print("Id should be 3 digits")
            return

        cm = input("Enter the flight company: ")
        st = int(input("Enter number of seats: "))
        pt = input("Enter pilot name: ")
        at = input("Enter airhostess name: ")
        av = input("Enter arrival point: ")
        dp = input("Enter departure point: ")

        cur.execute(
            "INSERT INTO flight VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (i, cm, st, av, dp, pt, at)
        )

        con.commit()
        con.close()
        print("Flight added successfully")

    # -------- MODIFY FLIGHT --------
    elif ch == 2:
        print("1. MODIFY COMPANY")
        print("2. MODIFY SEATS")
        print("3. MODIFY PILOT")
        print("4. MODIFY AIRHOSTESS")
        print("5. MODIFY ARRIVAL")
        print("6. MODIFY DEPARTURE")

        c = int(input("Enter your choice: "))

        i = int(input("Enter flight id: "))
        k = length(i)

        if k == 0:
            print("Flight not found")
            return

        if c == 1:
            new = input("Enter new company: ")
            cur.execute("UPDATE flight SET name=%s WHERE fid=%s", (new, i))

        elif c == 2:
            new = int(input("Enter new seats: "))
            cur.execute("UPDATE flight SET seats=%s WHERE fid=%s", (new, i))

        elif c == 3:
            new = input("Enter new pilot: ")
            cur.execute("UPDATE flight SET pilot=%s WHERE fid=%s", (new, i))

        elif c == 4:
            new = input("Enter new airhostess: ")
            cur.execute("UPDATE flight SET airhostess=%s WHERE fid=%s", (new, i))

        elif c == 5:
            new = input("Enter new arrival: ")
            cur.execute("UPDATE flight SET destination=%s WHERE fid=%s", (new, i))

        elif c == 6:
            new = input("Enter new departure: ")
            cur.execute("UPDATE flight SET departure=%s WHERE fid=%s", (new, i))

        else:
            print("Invalid choice")
            return

        con.commit()
        con.close()
        print("Flight updated successfully")

    # -------- DELETE FLIGHT --------
    elif ch == 3:
        i = int(input("Enter flight id to delete: "))
        k = length(i)

        if k == 0:
            print("Flight not found")
            return

        cur.execute("DELETE FROM flight WHERE fid=%s", (i,))
        con.commit()
        con.close()
        print("Flight deleted successfully")

    # -------- LIST FLIGHTS --------
    elif ch == 4:
        cur.execute("SELECT * FROM flight")
        data = cur.fetchall()

        if len(data) == 0:
            print("No flights available")
        else:
            print("ID   COMPANY   SEATS   ARRIVAL   DEPARTURE   PILOT   AIRHOSTESS")
            for row in data:
                print(row)

        con.close()

    # -------- SEARCH FLIGHT --------
    elif ch == 5:
        fid = int(input("Enter flight id: "))

        cur.execute("SELECT * FROM flight WHERE fid=%s", (fid,))
        data = cur.fetchone()

        if data:
            print("Id:", data[0])
            print("Company:", data[1])
            print("Seats:", data[2])
            print("Arrival:", data[3])
            print("Departure:", data[4])
            print("Pilot:", data[5])
            print("Airhostess:", data[6])
        else:
            print("Flight not found")

        con.close()

    else:
        print("Invalid choice")
