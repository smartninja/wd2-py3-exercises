from smartninja_sql.sqlite import SQLiteDatabase

chinook = SQLiteDatabase("Chinook_Sqlite.sqlite")  # download and save this DB first! (see readme.md)
# chinook.print_tables(verbose=True)

chinook.pretty_print("SELECT * FROM Album;")

chinook.pretty_print("SELECT * FROM Artist;")
