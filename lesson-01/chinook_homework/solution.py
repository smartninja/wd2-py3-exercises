from smartninja_sql.sqlite import SQLiteDatabase

chinook = SQLiteDatabase("Chinook_Sqlite.sqlite")  # download and save this DB first! (see readme.md)
chinook.print_tables(verbose=True)  # just to see the tables and fields in the database

print("----------------")

print("1) Write an SQL command that will print Name from the table Artist (for all the database objects).")
artist_names = chinook.execute("SELECT Artist.Name FROM Artist;")

for artist_name in artist_names:
    print(artist_name[0])

print("----------------")

print("2) Print all data from the table Invoice where BillingCountry is Germany.")
invoices_de = chinook.execute("""
                                SELECT *
                                FROM Invoice
                                WHERE  Invoice.BillingCountry = 'Germany';
                                """)

for invoice in invoices_de:
    print(invoice)

print("----------------")

print("3) Count how many albums are in the database.")

album_num = chinook.execute("SELECT COUNT(*) FROM Album;")
print(album_num)
print(album_num[0][0])

print("----------------")

print("4) How many customers are from France?")

fr_num = chinook.execute("""
                            SELECT COUNT(*)
                            FROM Customer
                            WHERE Customer.Country = 'France';
                            """)
print(fr_num[0][0])
