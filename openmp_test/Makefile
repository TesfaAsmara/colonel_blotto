SHELL=/bin/bash
TEST_SIZES := 1000 5000 10000 20000 50000

.PHONY: all

all: omp_demo_file demo_file

omp_demo_file: omp_demo_file.c
	gcc -fopenmp -g -pg -O3 -o omp_demo_file omp_demo_file.c

demo_file: demo_file.c
	gcc -fopenmp -g -pg -O3 -o demo_file demo_file.c

test: omp_demo_file demo_file
	@for size in $(TEST_SIZES); do \
		echo "-------------------"; \
		echo "-------------------"; \
		echo "Serial:";\
		time ./demo_file $$size;\
		echo "-------------------"; \
		export OMP_NUM_THREADS=4; \
		echo "Parallel with $$OMP_NUM_THREADS threads"; \
		time ./omp_demo_file $$size;\
		echo "-------------------"; \
		echo "-------------------"; \
		echo "";\
	done

clean:
	rm -f demo_file omp_demo_file || true
	rm *.txt || true
	rm gmon.out

# veryclean: clean
