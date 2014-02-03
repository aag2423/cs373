all:
	make Collatz.zip

clean:
	rm -f *.pyc
	rm -f Collatz.html
	rm -f Collatz.log
	rm -f Collatz.zip
	rm -f RunCollatz.out
	rm -f RunCollatz.tmp
	rm -f TestCollatz.out

diff: RunCollatz.in RunCollatz.py Collatz.py
	RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	diff RunCollatz.out RunCollatz.tmp
	rm RunCollatz.tmp

turnin-list:
	turnin --list thunt cs373pj1

turnin-submit: Collatz.zip
	turnin --submit thunt cs373pj1 Collatz.zip

turnin-verify:
	turnin --verify thunt cs373pj1

Collatz.html: Collatz.py
	pydoc -w Collatz

Collatz.log: Collatz.py
	git log > Collatz.log

Collatz.zip: makefile                                   \
             Collatz.html Collatz.log Collatz.py        \
             RunCollatz.in RunCollatz.out RunCollatz.py \
             SphereCollatz.py                           \
             TestCollatz.py TestCollatz.out
	zip -r Collatz.zip                                \
           makefile                                   \
           Collatz.html Collatz.log Collatz.py        \
           RunCollatz.in RunCollatz.out RunCollatz.py \
           SphereCollatz.py                           \
           TestCollatz.py TestCollatz.out

RunCollatz.out: RunCollatz.in RunCollatz.py Collatz.py
	RunCollatz.py < RunCollatz.in > RunCollatz.out

TestCollatz.out: TestCollatz.py Collatz.py
	TestCollatz.py >& TestCollatz.out
