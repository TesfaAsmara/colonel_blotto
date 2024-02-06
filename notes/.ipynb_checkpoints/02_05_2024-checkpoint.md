
- wrote tournament code in C
    - refactored the read_strategies method into the tournament method
        - note that in order to pass a 2D multidimensional array to a function
       in C, you must specify the number of entries for every index after the first.
    - notice that we cannot actually compute the max number of configurations
      because the `long long` integer is not big enough for the expressions in the computation.
- wrote Makefile
- wrote command line interface for both python and C code
- wrote execution profiling code