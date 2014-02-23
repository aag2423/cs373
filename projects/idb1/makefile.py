all:
	make IDB1.zip

clean:
	rm -f *.pyc
	rm -f IDB1.html
	rm -f IDB1.log
	rm -f IDB1.zip

turnin-list:
	turnin --list acoomans cs373pj3

turnin-submit: IDB1.zip
	turnin --submit acoomans cs373pj3 IDB1.zip

turnin-verify:
	turnin --verify acoomans cs373pj3

IDB.html: IDB.py
	epydoc IDB

IDB1.log:
	git log > IDB1.log

IDB1.zip: makefile apiary.apib \
           IDB.html IDB.log    \
           IDB1.py IDB1.pdf    \
           TestIDB1.py
	zip -r IDB1.zip             \
	       makefile apiary.apib \
	       IDB.html IDB.log     \
	       IDB1.py IDB1.pdf     \
	       TestIDB1.py
