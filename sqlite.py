import sqlite3

createDb = sqlite3.connect('sample.db')

queryCurs = createDb.cursor()

def createTable():
	queryCurs.execute('''CREATE TABLE customers
		(id INTEGER PRIMARY KEY, name TEXT, street TEXT, city TEXT, state TEXT, balace REAL)''')

def addCustomer(name, street, city, state, balace):
	queryCurs.execute('''INSTERT INTO  customers (name, street,city,state,balace)
		VALUES (?,?,?,?,?)''',(name, street,city,state,balace) )
def main():
	createTable()

	addCustomer('Derek Banas', '233 Highway Ave', 'Verona', 'PA', 150.67)
	addCustomer('Derek Banas', '233 Highway Ave', 'Verona', 'PA', 150.67)
	addCustomer('Derek Banas', '233 Highway Ave', 'Verona', 'PA', 150.67)
	addCustomer('Derek Banas', '233 Highway Ave', 'Verona', 'PA', 150.67)

	createDb.commit()

	queryCurs.execute('SELECT * FROM customers')

	listTitle = ['Id Num', 'Name', 'Street', 'City', 'State', 'Balance']

	for i in queryCurs:
		print "\n"
		for j in i:
			print j

if __name__ == '__main__': main()