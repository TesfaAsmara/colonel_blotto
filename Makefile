SHELL := /bin/bash
CASTLES=10
TROOPS=1 10

.PHONY: all run_blotto run_sums profile_blotto profile_sums

all: blotto sums

blotto: blotto.c
	gcc -g -Wall -Wextra -pg -O3 -march=native -funroll-loops -flto -o blotto blotto.c
# gcc -pg -O3 -o blotto blotto.c

sums: sums.c
	gcc -g -Wall -Wextra -pg -O3 -march=native -funroll-loops -flto -o sums sums.c

run_blotto: blotto
	./blotto -c 2 -t 10

run_sums: sums
	./sums -c 2 -t 10

profile_blotto: run_blotto
	gprof blotto gmon.out > blotto_analysis.txt
	cat blotto_analysis.txt

profile_sums: run_sums
	gprof sums gmon.out > sums_analysis.txt
	cat sums_analysis.txt

profile_sums_py: sums.py
	python -m cProfile -s cumtime sums.py > sums_py_analysis.txt
	cat sums_py_analysis.txt

profile_all:
	mkdir -p profiling
	$(foreach troop,$(TROOPS),\
		echo "Running for $(CASTLES) castles and $(troop) troops";\
		{ time ./sums -c $(CASTLES) -t $(troop); } > profiling/sums_c_$(CASTLES)_t_$(troop)_profile.txt 2>&1;\
		{ time ./blotto -c $(CASTLES) -t $(troop); } > profiling/blotto_c_$(CASTLES)_t_$(troop)_profile.txt 2>&1;\
        { time python blotto_jit.py -c $(CASTLES) -t $(troop); } > profiling/blotto_jit_py_c_$(CASTLES)_t_$(troop)_profile.txt 2>&1;\
		{ time python slowest_blotto.py -c $(CASTLES) -t $(troop); } > profiling/slowest_blotto_py_c_$(CASTLES)_t_$(troop)_profile.txt 2>&1;\
	) \
	python plot_profiling.py


clean:
	rm -f blotto sums gmon.out
	rm -rf profiling