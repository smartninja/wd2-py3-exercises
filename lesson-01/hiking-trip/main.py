from smartninja_sql.sqlite import SQLiteDatabase

# create database
db = SQLiteDatabase()  # database saved in RAM (is deleted after program ends)
# db = SQLiteDatabase("hiking.sqlite")  # database stored on disk

# create a User table
db.execute("""CREATE TABLE IF NOT EXISTS User(
                id integer primary key autoincrement, 
                name text, 
                age integer);
            """)

db.print_tables(verbose=True)

# insert data into table
db.execute("INSERT INTO User(name, age) VALUES ('Matt', 31);")

# query data from the table
result = db.execute("SELECT * FROM User;")
print(result)

# update data in the table
db.execute("""
            UPDATE User 
            SET age=22 
            WHERE id=1;
            """)

result = db.execute("SELECT * FROM User;")
print(result)

# delete object/row from the table
db.execute("""
            DELETE FROM User 
            WHERE id=1;
            """)

result = db.execute("SELECT * FROM User;")
print(result)

# add new table column
db.execute("""
            ALTER TABLE User 
            ADD email text;
            """)

db.execute("INSERT INTO User(name, age, email) VALUES ('Matt', 31, 'matt@smartninja.org');")

result = db.execute("SELECT * FROM User;")
print(result)

# delete table
print("Tables before deletion: ")
db.print_tables()

db.execute("DROP TABLE User;")

print("Tables after deletion: ")
db.print_tables()
