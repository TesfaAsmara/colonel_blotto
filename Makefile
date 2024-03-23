SHELL := /bin/bash
CASTLES= 3
TROOPS= 100 90 80 70 60 50 40 30 20
PROFILE_DIR = profiling

.PHONY: all run_blotto run_sums profile_blotto profile_sums

all: blotto sums blotto_parallel

blotto: blotto.c
	gcc -fopenmp -g -Wall -Wextra -pg -O3 -march=native -funroll-loops -flto -o blotto blotto.c
# gcc -pg -O3 -o blotto blotto.c

blotto_parallel: blotto_tmp_parallel.c
	gcc -fopenmp -g -Wall -Wextra -pg -O3 -march=native -funroll-loops -flto -o blotto_parallel blotto_tmp_parallel.c

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

profile: create_files run_commands plot

create_files:
	mkdir -p $(PROFILE_DIR)
	$(foreach castle, $(CASTLES), \
		$(foreach troop, $(TROOPS), \
			touch $(PROFILE_DIR)/sums_c_$(castle)_t_$(troop)_profile.txt; \
			touch $(PROFILE_DIR)/blotto_c_$(castle)_t_$(troop)_profile.txt; \
            touch $(PROFILE_DIR)/blotto_parallel_c_$(castle)_t_$(troop)_profile.txt; \
			touch $(PROFILE_DIR)/blotto_jit_py_c_$(castle)_t_$(troop)_profile.txt; \
			touch $(PROFILE_DIR)/blotto_jit_parallel_py_c_$(castle)_t_$(troop)_profile.txt; \
			touch $(PROFILE_DIR)/slowest_blotto_py_c_$(castle)_t_$(troop)_profile.txt; \
		) \
	)

run_commands:
	$(foreach castle, $(CASTLES), \
		$(foreach troop, $(TROOPS), \
			echo "Running for $(castle) castles and $(troop) troops"; \
			{ time ./sums -c $(castle) -t $(troop); } > $(PROFILE_DIR)/sums_c_$(castle)_t_$(troop)_profile.txt 2>&1; \
			{ time ./blotto -c $(castle) -t $(troop); } > $(PROFILE_DIR)/blotto_c_$(castle)_t_$(troop)_profile.txt 2>&1; \
            { time ./blotto_parallel -c $(castle) -t $(troop); } > $(PROFILE_DIR)/blotto_parallel_c_$(castle)_t_$(troop)_profile.txt 2>&1; \
			{ time python blotto_jit.py -c $(castle) -t $(troop); } > $(PROFILE_DIR)/blotto_jit_py_c_$(castle)_t_$(troop)_profile.txt 2>&1; \
			{ time python blotto_jit_parallel.py -c $(castle) -t $(troop); } > $(PROFILE_DIR)/blotto_jit_parallel_py_c_$(castle)_t_$(troop)_profile.txt 2>&1; \
			{ time python slowest_blotto.py -c $(castle) -t $(troop); } > $(PROFILE_DIR)/slowest_blotto_py_c_$(castle)_t_$(troop)_profile.txt 2>&1; \
		) \
	)

plot:
	python plot_profiling.py



clean:
	rm -f blotto sums gmon.out
	rm -rf profiling