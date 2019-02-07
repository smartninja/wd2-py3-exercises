### Exercises 2.1 (Relationships)

a) What **order** was the most **expensive**? Which one was the **cheapest**?

The most expensive:

	SELECT MAX(Invoice.Total), *
	FROM Invoice;

The cheapest:

	SELECT MIN(Invoice.Total), *
	FROM Invoice;

b) Which **city** had the **most orders**?

	SELECT Invoice.BillingCity, COUNT(*) AS Invoice_num
	FROM Invoice
	GROUP BY Invoice.BillingCity
	ORDER BY Invoice_num DESC;

c) Calculate (or count) how many tracks have this MediaType: **Protected AAC audio file**.

Solution 1)

	SELECT COUNT(*)
	FROM Track
	JOIN MediaType ON Track.MediaTypeId=MediaType.MediaTypeId
	WHERE MediaType.Name='Protected AAC audio file';

Solution 2)

	SELECT MediaType.Name, COUNT(*)
	FROM Track
	JOIN MediaType ON MediaType.MediaTypeId = Track.MediaTypeId
	GROUP BY Track.MediaTypeId;

d) Find out what **Artist** has the **most albums**?

Solution 1)

	SELECT Artist.Name, COUNT(*) as Album_num
	FROM Artist
	JOIN Album ON Album.ArtistId = Artist.ArtistId
	GROUP BY Album.ArtistId
	ORDER BY Album_num DESC;

Solution 2)

	SELECT COUNT(Artist.Name) AS Alb_count, Artist.Name AS Art_name 
	FROM Artist
	INNER JOIN Album ON Album.ArtistId=Artist.ArtistId
	GROUP BY Artist.ArtistId
	ORDER BY -COUNT(Artist.Name)

e) What **genre** has the **most tracks**?

	SELECT Genre.Name, COUNT(*) as Track_num
	FROM Genre
	JOIN Track ON Track.GenreId = Genre.GenreId
	GROUP BY Track.GenreId
	ORDER BY Track_num DESC;

f) Which **customer** spent the **most money** so far?

	SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS Invoice_sum
	FROM Customer
	JOIN Invoice ON Invoice.CustomerId = Customer.CustomerId
	GROUP BY Invoice.CustomerId
	ORDER BY Invoice_sum DESC;

g) What **songs** were bought with each **order**? (hint: here you have to do a many-to-many SQL query with three tables: Track, Invoice and InvoiceLine. You have to do two JOINS here)

	SELECT Invoice.InvoiceId, Track.Name
	FROM Invoice
	JOIN InvoiceLine ON InvoiceLine.InvoiceId = Invoice.InvoiceId
	JOIN Track ON InvoiceLine.TrackId = Track.TrackId;