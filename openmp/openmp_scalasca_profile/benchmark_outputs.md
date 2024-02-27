skin gcc -fopenmp -O3 -o blotto_omp blotto_omp.c
-> /opt/scorep/bin//scorep gcc -fopenmp -O3 -o blotto_omp blotto_omp.c
skin gcc -fopenmp -O3 -o blotto_omp_single_output blotto_omp_single_output.c
-> /opt/scorep/bin//scorep gcc -fopenmp -O3 -o blotto_omp_single_output blotto_omp_single_output.c
skin gcc -fopenmp -O3 -o blotto blotto.c
-> /opt/scorep/bin//scorep gcc -fopenmp -O3 -o blotto blotto.c
gcc -g -Wall -Wextra -pg -O3 -march=native -funroll-loops -flto -o sums sums.c
if [[ ! -d "./configurations" ]]; then \
	mkdir ./configurations; \
fi
if [[ ! -d "./results" ]]; then \
	mkdir ./results; \
fi
Comparing -c 6 -t 21
S=C=A=N: Scalasca 2.6.1 runtime summarization
S=C=A=N: ./scorep_blotto_O_sum experiment archive
S=C=A=N: Sun Feb 25 17:33:59 2024: Collect start
 ./blotto -c 6 -t 21
S=C=A=N: Sun Feb 25 17:40:27 2024: Collect done (status=0) 388s
S=C=A=N: ./scorep_blotto_O_sum complete.
With 4 threads
Single output
S=C=A=N: Scalasca 2.6.1 runtime summarization
S=C=A=N: ./scorep_blotto_omp_single_output_Ox4_sum experiment archive
S=C=A=N: Sun Feb 25 17:40:28 2024: Collect start
 ./blotto_omp_single_output -c 6 -t 21
Num threads: 4 
S=C=A=N: Sun Feb 25 17:50:34 2024: Collect done (status=0) 606s
S=C=A=N: ./scorep_blotto_omp_single_output_Ox4_sum complete.
 2163471310  2163471310 30498052970 output_omp_single_output.txt
Multi outputs
S=C=A=N: Scalasca 2.6.1 runtime summarization
S=C=A=N: ./scorep_blotto_omp_Ox4_sum experiment archive
S=C=A=N: Sun Feb 25 17:52:34 2024: Collect start
 ./blotto_omp -c 6 -t 21
Num threads: 4 
S=C=A=N: Sun Feb 25 17:54:14 2024: Collect done (status=0) 100s
S=C=A=N: ./scorep_blotto_omp_Ox4_sum complete.

Compare the outcomes
  553472974   553472974  7787452471 output_omp_t0.txt
  545054720   545054720  7667942159 output_omp_t1.txt
  536666112   536666112  7563652952 output_omp_t2.txt
  528277504   528277504  7479005388 output_omp_t3.txt
 2163471310  2163471310 30498052970 total

 2163471310  2163471310 30498052970 output.txt

ls -lh *.txt
-rw-rw-r-- 1 ykim ykim  29G Feb 25 17:50 output_omp_single_output.txt
-rw-rw-r-- 1 ykim ykim 7.3G Feb 25 17:54 output_omp_t0.txt
-rw-rw-r-- 1 ykim ykim 7.2G Feb 25 17:54 output_omp_t1.txt
-rw-rw-r-- 1 ykim ykim 7.1G Feb 25 17:54 output_omp_t2.txt
-rw-rw-r-- 1 ykim ykim 7.0G Feb 25 17:54 output_omp_t3.txt
-rw-rw-r-- 1 ykim ykim  29G Feb 25 17:40 output.txt
