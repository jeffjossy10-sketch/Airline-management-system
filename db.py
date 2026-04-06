import mysql.connector as mc
def get_connection():
    try:
        con=mc.connect(host="localhost",user="root",passwd="tiger",database="infinix")
        return con
    except:
        print("Error connecting to database")
        
    
