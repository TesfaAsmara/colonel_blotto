SHELL=/bin/bash
CASTLES=6
TROOPS=10 15
SUMS_OUTPUT_DIR=./configurations
RESULT_DIR=./results
TEST_SIZES := 10 13 

.PHONY: all run_blotto run_sums profile_blotto profile_sums

all: blotto_omp sums

blotto_omp: blotto_omp.c
	gcc -fopenmp -g -pg -O3 -o blotto_omp blotto_omp.c

blotto: blotto.c
	gcc -g -Wall -Wextra -pg -O3 -march=native -funroll-loops -flto -o blotto blotto.c
# gcc -pg -O3 -o blotto blotto.c

sums: sums.c
	gcc -g -Wall -Wextra -pg -O3 -march=native -funroll-loops -flto -o sums sums.c

make_dirs: 
	if [[ ! -d "$(SUMS_OUTPUT_DIR)" ]]; then \
		mkdir $(SUMS_OUTPUT_DIR); \
	fi

	if [[ ! -d "$(RESULT_DIR)" ]]; then \
		mkdir $(RESULT_DIR); \
	fi

run_blotto: blotto
	./blotto -c 2 -t 10

run_blotto_omp: blotto_omp
	./blotto_omp -c 2 -t 10

run_sums: sums
	./sums -c 6 -t 10

test: blotto_omp blotto sums make_dirs
	@for size in $(TEST_SIZES); do \
		echo "Comparing -c 6 -t $$size"; \
		./sums -c 6 -t $$size; \
		time ./blotto -c 6 -t $$size; \
		export OMP_NUM_THREADS=4; \
		echo "Using $$OMP_NUM_THREADS threads"; \
		time ./blotto_omp -c 6 -t $$size;\
		echo ""; \
		echo "Compare the outcomes";\
		wc output_omp_t*; echo "";  \
		wc output.txt; echo "";\
		# Uncomment the next line to compare the serical and openmp results; \
		# It may take some time to sort and diff;\
		# The diff result should be 0;\
		# sort -V output_omp_t* > sorted.txt && diff sorted.txt output.txt | wc; \
	done
	ls -lh *.txt

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
	rm -f blotto_omp blotto_acc
	rm -rf profiling

veryclean: clean
	rm -rf $(SUMS_OUTPUT_DIR)
	rm -rf $(RESULT_DIR)
	rm -rf *.dSYM
	rm -rf *.txt