import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='6773', host='localhost')
cursor = conn.cursor()
print(conn.get_dsn_parameters(), "\n")
cursor.execute('INSERT INTO Customers (Id, '
               'FirstName, LastName, '
               'Email, Phone, Age) '
               "VALUES (2, 'Andrei', 'Sokolov', 'sokolov@yandex.ru', '+7113261233', 29);")
conn.commit()
cursor.close()
conn.close()
