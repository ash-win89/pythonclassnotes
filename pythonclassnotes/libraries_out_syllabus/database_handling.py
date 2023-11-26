'''
#1.example
import sqlite3
conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("CREATE TABLE user (name text, age integer)")
c.execute("INSERT INTO user VALUES ('User A', 42)")
c.execute("INSERT INTO user VALUES ('User B', 43)")
conn.commit()
c.execute("SELECT * FROM user")
print(c.fetchall())
conn.close()
'''
#2.example

import sqlite3
stocks = [('2006-01-05', 'BUY', 'RHAT', 100, 35.14),
('2006-03-28', 'BUY', 'IBM', 1000, 45.0),
('2006-04-06', 'SELL', 'IBM', 500, 53.0),
('2006-04-05', 'BUY', 'MSFT', 1000, 72.0)]
conn = sqlite3.connect(":memory:")
conn.execute("create table stocks (date text, buysell text, symb text, amount int, pricereal)")
conn.executemany("insert into stocks values (?, ?, ?, ?, ?)", stocks)
cur = conn.cursor()
for row in cur.execute('SELECT * FROM stocks ORDER BY pricereal'):
    print(row)


'''
isolation_level
It is an attribute used to get or set the current isolation level. None for autocommit mode or one of DEFERRED ,
IMMEDIATE or EXCLUSIVE .

cursor
The cursor object is used to execute SQL commands and queries.

commit()
Commits the current transaction

rollback()
Rolls back any changes made since the previous call to commit()

close()
Closes the database connection. It does not call commit() automatically. If close() is called without ﬁrst
calling commit() (assuming you are not in autocommit mode) then all changes made will be lost.

total_changes
An attribute that logs the total number of rows modiﬁed, deleted or inserted since the database was opened.


execute , executemany , and executescript
These functions perform the same way as those of the cursor object. This is a shortcut since calling these
functions through the connection object results in the creation of an intermediate cursor object and calls the
corresponding method of the cursor object

row_factory
You can change this attribute to a callable that accepts the cursor and the original row as a tuple and will
return the real result row.
def dict_factory(cursor, row):
d = {}
for i, col in enumerate(cursor.description):
d[col[0]] = row[i]
return d
conn = sqlite3.connect(":memory:")
conn.row_factory = dict_factory

This is how the data types are converted when moving from SQL to Python or vice versa.
None =NULL
int =INTEGER/INT
float = REAL/FLOAT
str = TEXT/VARCHAR(n)
bytes = BLOB

'''