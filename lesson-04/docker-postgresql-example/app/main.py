import psycopg2

conn = psycopg2.connect(dbname="mydatabase", user="user", password="pass", host="localhost")

cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS article (
title text, 
words_num integer);
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS "user" (
name text, 
age integer);
''')

cur.execute('''
INSERT INTO "user" ("name", "age")
VALUES ('Matej', 31);
''')

cur.execute('''INSERT INTO "article" (title, words_num) VALUES ('A story about PostgreSQL', 500);''')

cur.execute('''SELECT * FROM "user";''')
result = cur.fetchone()
print(result)

cur.execute('''SELECT * FROM article;''')
result2 = cur.fetchone()
print(result2)

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
