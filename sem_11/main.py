import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='6773', host='localhost')
cursor = conn.cursor()
print(conn.get_dsn_parameters(), "\n")
cursor.execute('CREATE TABLE Customers(Id SERIAL PRIMARY KEY, '
               'FirstName CHARACTER VARYING(20), LastName CHARACTER VARYING(20), '
               'Email CHARACTER VARYING(30) UNIQUE, Phone CHARACTER VARYING(30) '
               'UNIQUE, Age INTEGER);')
conn.commit()
cursor.close()
conn.close()
