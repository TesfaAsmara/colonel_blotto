ITERATIONS = 10
SHELL := /bin/bash
CASTLES= 2
TROOPS= 5 10 20 30 40 50 60 70 80 90 100
PROFILE_DIR = profiling

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
