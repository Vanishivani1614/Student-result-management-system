import sqlite3

def create_db():
    # Using a context manager to ensure proper opening and closing of the connection
    con=sqlite3.connect(database="rms.db") 
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text, duration text, charges int, description text)")
    con.commit()
   
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, dob text,contact text,addmission text,course text,state text,city text,pin text,adderss text)")
    con.commit() 
    
    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT, roll text, name text, course text, marks_ob text,full_marks text,per text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, f_name text,l_name text,contact text,email text,question text,answer text,password text)")
    con.commit()
    
    
        # No need to call con.commit() when using a context manager
    con.close()
# Call the function to create the database and table
create_db()
