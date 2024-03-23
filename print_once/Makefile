ITERATIONS = 10
SHELL := /bin/bash
CASTLES= 3
TROOPS= 100
PROFILE_DIR = profiling
 

all: blotto sums blotto_parallel

blotto: blotto.c
	gcc -fopenmp -g -Wall -Wextra -pg -O3 -march=native -funroll-loops -flto -o blotto blotto.c
# gcc -pg -O3 -o blotto blotto.c 4 5 6 7 8 9 10

blotto_parallel: blotto_tmp_parallel.c
	gcc -fopenmp -g -Wall -Wextra -pg -O3 -march=native -funroll-loops -flto -o blotto_parallel blotto_tmp_parallel.c

sums: sums.c
	gcc -g -Wall -Wextra -pg -O3 -march=native -funroll-loops -flto -o sums sums.c

blotto_ps: blotto_point_system.c
	gcc -fopenmp -g -Wall -Wextra -pg -O3 -march=native -funroll-loops -flto -o blotto_ps blotto_point_system.c

create_configs:
	$(foreach castle, $(CASTLES), \
		$(foreach troop, $(TROOPS), \
				{ time ./sums -c $(castle) -t $(troop); } >> $(PROFILE_DIR)/sums_c_$(castle)_t_$(troop)_profile.txt 2>&1; \
		) \
	)

run_blotto:
	$(foreach castle, $(CASTLES), \
		$(foreach troop, $(TROOPS), \
				{ time ./blotto -c $(castle) -t $(troop); } >> $(PROFILE_DIR)/blotto_c_$(castle)_t_$(troop)_profile.txt 2>&1; \
		) \
	)

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
			$(foreach iter, $(shell seq 1 $(ITERATIONS)), \
				echo "Running iteration $(iter) for $(castle) castles and $(troop) troops"; \
				{ time ./sums -c $(castle) -t $(troop); } >> $(PROFILE_DIR)/sums_c_$(castle)_t_$(troop)_profile.txt 2>&1; \
				{ time ./blotto -c $(castle) -t $(troop); } >> $(PROFILE_DIR)/blotto_c_$(castle)_t_$(troop)_profile.txt 2>&1; \
				{ time ./blotto_parallel -c $(castle) -t $(troop); } >> $(PROFILE_DIR)/blotto_parallel_c_$(castle)_t_$(troop)_profile.txt 2>&1; \
				{ time python blotto_jit.py -c $(castle) -t $(troop); } >> $(PROFILE_DIR)/blotto_jit_py_c_$(castle)_t_$(troop)_profile.txt 2>&1; \
				{ time python blotto_jit_parallel.py -c $(castle) -t $(troop); } >> $(PROFILE_DIR)/blotto_jit_parallel_py_c_$(castle)_t_$(troop)_profile.txt 2>&1; \
				{ time python slowest_blotto.py -c $(castle) -t $(troop); } >> $(PROFILE_DIR)/slowest_blotto_py_c_$(castle)_t_$(troop)_profile.txt 2>&1; \
			) \
		) \
	)

plot:
	python plot_profiling_3.py
