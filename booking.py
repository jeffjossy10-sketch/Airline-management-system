from db import get_connection


def booking():
    con = get_connection()
    if not con:
        print("Connection failed")
        return

    cur = con.cursor()

    print("------ BOOKING SECTION ------")
    print("1. Book Flight")
    print("2. Delete Booking")

    y = int(input("Enter your choice: "))

    # -------- BOOK FLIGHT --------
    if y == 1:
        while True:
            print("\n------ BOOKING MENU ------")
            print("1. List Customers")
            print("2. List Flights")
            print("3. Proceed to Booking")
            print("4. Exit")

            x = int(input("Enter your choice: "))

            # ---- SHOW CUSTOMERS ----
            if x == 1:
                cur.execute("SELECT * FROM customer")
                res = cur.fetchall()

                if not res:
                    print("No customers found")
                else:
                    for i in res:
                        print("ID:", i[0], "Name:", i[1])

            # ---- SHOW FLIGHTS ----
            elif x == 2:
                cur.execute("SELECT * FROM flight")
                data = cur.fetchall()

                if not data:
                    print("No flights available")
                else:
                    print("ID   COMPANY   SEATS   ARRIVAL   DEPARTURE")
                    for i in data:
                        print(i[0], i[1], i[2], i[3], i[4])

            # ---- BOOKING LOGIC ----
            elif x == 3:
                price = 0

                Booking_id = int(input("Enter Booking Id (3 digits): "))
                if len(str(Booking_id)) != 3:
                    print("Invalid Booking Id")
                    return

                cur.execute("SELECT * FROM booking WHERE Booking_id=%s", (Booking_id,))
                if cur.fetchone():
                    print("Booking ID already exists")
                    return

                Id = int(input("Enter Customer Id: "))
                cur.execute("SELECT * FROM customer WHERE c_id=%s", (Id,))
                if not cur.fetchone():
                    print("Customer not found")
                    return

                Flight = int(input("Enter Flight Id: "))
                cur.execute("SELECT * FROM flight WHERE fid=%s", (Flight,))
                if not cur.fetchone():
                    print("Flight not found")
                    return

                seat = int(input("Enter number of seats: "))
                price += seat * 5000

                Weight = int(input("Enter luggage weight: "))
                if Weight > 50:
                    extra = Weight - 50
                    print("Extra weight:", extra)
                    print("Extra charge:", extra * 300)
                    price += (extra * 300) + 1000
                else:
                    price += 1000

                pet_choice = input("Include pets (y/n): ")
                if pet_choice in 'Yy':
                    price += 2500
                    Pet = 'Y'
                else:
                    Pet = 'N'

                cur.execute(
                    "INSERT INTO booking VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (Booking_id, Id, Flight, seat, Weight, Pet, price)
                )

                con.commit()
                print("Booking successful")
                print("Total price:", price)

            elif x == 4:
                break

            else:
                print("Invalid choice")

    # -------- DELETE BOOKING --------
    elif y == 2:
        id1 = int(input("Enter Booking Id: "))

        if len(str(id1)) != 3:
            print("Invalid Booking Id")
            return

        cur.execute("SELECT * FROM booking WHERE Booking_id=%s", (id1,))
        if not cur.fetchone():
            print("Booking not found")
            return

        cur.execute("DELETE FROM booking WHERE Booking_id=%s", (id1,))
        con.commit()
        con.close()

        print("Booking deleted successfully")

    else:
        print("Invalid choice")
