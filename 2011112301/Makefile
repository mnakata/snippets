all:

test: rand1.dat rand2.dat rand3.dat

rand1.dat: rand1.py
	time ./$< | tee $@

rand2.dat: rand2.py
	time ./$< | tee $@

rand3.dat: rand3.py
	time ./$< | tee $@

clean:
	$(RM) *~

distclean: clean
	$(RM) *.dat