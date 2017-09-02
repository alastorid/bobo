all: liu.db

liu.db: liu.txt output.txt header.txt
	cat header.txt output.txt > /tmp/tmp_db.txt
	ibus-table-createdb -s /tmp/tmp_db.txt -n liu.db
	rm /tmp/tmp_db.txt
	@echo "Use 'make install' to install lib to your ibus table"

output.txt: assets
	@python wordfreq.py
	#@sort /tmp/output.txt > output.txt
clean:
	rm -f liu.db output.txt

install: liu.db
	install -m 0755 liu.db /usr/share/ibus-table/tables/
	#install -m 0755 liu.svg /usr/share/ibus-table/icons/
reload:
	ibus restart
