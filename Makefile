all: liu.db


liu.db: liu.txt
	ibus-table-createdb -s liu.txt -n liu.db
