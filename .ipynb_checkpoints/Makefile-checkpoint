.PHONY: all run_blotto run_sums profile_blotto profile_sums

all: blotto sums

blotto: blotto.c
	gcc -g -Wall -Wextra -pg -O3 -march=native -funroll-loops -flto -o blotto blotto.c
# gcc -pg -O3 -o blotto blotto.c

sums: sums.c
	gcc -g -Wall -Wextra -pg -O3 -march=native -funroll-loops -flto -o sums sums.c

run_blotto: blotto
	./blotto

run_sums: sums
	./sums

profile_blotto: run_blotto
	gprof blotto gmon.out > blotto_analysis.txt
	cat blotto_analysis.txt

profile_sums: run_sums
	gprof sums gmon.out > sums_analysis.txt
	cat sums_analysis.txt

profile_sums_py: sums.py
	python -m cProfile -s cumtime sums.py > sums_py_analysis.txt
	cat sums_py_analysis.txt
