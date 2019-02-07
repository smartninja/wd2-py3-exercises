### Homework 1.1 (Chinook) solutions

Download this database: [Chinook.sqlite](https://storage.googleapis.com/smartninja-org-assets/curriculums/sql/Chinook_Sqlite.sqlite)

1) This database has many tables. Write an SQL command that will print **Name** from the table **Artist** (for all the database entries).

	SELECT Artist.Name
	FROM Artist;

2) Print all data from the table **Invoice** where `BillingCountry` is **Germany**.

	SELECT *
	FROM Invoice
	WHERE  Invoice.BillingCountry = 'Germany';

3) Count how many **albums** are in the database. Look into the SQL documentation for help: [http://www.w3schools.com/sql/sql_functions.asp](http://www.w3schools.com/sql/sql_functions.asp)).

	SELECT COUNT(*)
	FROM Album;

4) How many customers are from France?

	SELECT COUNT(*)
	FROM Customer
	WHERE Customer.Country = 'France';
