all:
	make IDB.zip

clean:
	rm -f *.pyc
	rm -f Models.html
	rm -f IDB.log
	rm -f IDB.zip

turnin-list:
	turnin --list acoomans cs373pj3

turnin-submit: IDB.zip
	turnin --submit acoomans cs373pj3 IDB.zip

turnin-verify:
	turnin --verify acoomans cs373pj3

Models.html: Models.py
	epydoc IDB

IDB.log:
	git log > IDB.log

IDB.zip: makefile apiary.apib   \
         Models.html Models.py  \
         IDB.log     Report.pdf \
         test.py
	zip -r IDB.zip                 \
           makefile    apiary.apib \
           Models.html Models.py   \
           IDB.log     Report.pdf  \
           test.py
