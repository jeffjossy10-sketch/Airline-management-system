from customer import customer
from flight import flight
from employee import employee
from booking import booking
import mysql.connector as mc
import sys


def dbms():
    con = mc.connect(host='localhost', user='root', passwd='tiger')
    if con.is_connected():
        cur = con.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS infinix")
        con.commit()
        print("Database created successfully")
        con.close()


def ctables():
    con = mc.connect(host='localhost', user='root', passwd='tiger', database='infinix')
    cur = con.cursor()

    print("TABLES")
    print("(1) EMPLOYEE")
    print("(2) CUSTOMER")
    print("(3) FLIGHT")
    print("(4) BOOKING")

    ch = input("Create tables? (Y/N): ")

    if ch in 'Yy':
        cur.execute("CREATE TABLE IF NOT EXISTS emp(empid INT PRIMARY KEY, name VARCHAR(35), contact VARCHAR(10), gender CHAR(1), address VARCHAR(100), age INT)")
        cur.execute("CREATE TABLE IF NOT EXISTS customer(c_id INT PRIMARY KEY, name VARCHAR(30), contact VARCHAR(10), address VARCHAR(100), passport INT, age INT)")
        cur.execute("CREATE TABLE IF NOT EXISTS flight(fid INT PRIMARY KEY, name VARCHAR(30), seats INT, destination VARCHAR(25), departure VARCHAR(25), pilot VARCHAR(20), airhostess VARCHAR(20))")
        cur.execute("CREATE TABLE IF NOT EXISTS booking(booking_id INT PRIMARY KEY, id INT, flight INT, seat INT, weight INT, pet CHAR(1), price INT)")

        con.commit()
        print("Tables created successfully")

    con.close()


def listtables():
    con = mc.connect(host='localhost', user='root', passwd='tiger', database='infinix')
    cur = con.cursor()

    cur.execute("SHOW TABLES")
    res = cur.fetchall()

    if not res:
        print("No tables found")
    else:
        for i in res:
            print(i[0])

    con.close()


# -------- MAIN LOOP --------
while True:
    print("\nINFINIX AIRPORT MANAGEMENT SYSTEM")
    print("1. Customer")
    print("2. Booking")
    print("3. Employee")
    print("4. Flight")
    print("5. Create Database")
    print("6. Create Tables")
    print("7. List Tables")
    print("8. Exit")

    ch = input("Enter choice: ")

    if ch == '1':
        customer()
    elif ch == '2':
        booking()
    elif ch == '3':
        employee()
    elif ch == '4':
        flight()
    elif ch == '5':
        dbms()
    elif ch == '6':
        ctables()
    elif ch == '7':
        listtables()
    elif ch == '8':
        print("Thankyou")
        sys.exit()
    else:
        print("Invalid choice")
