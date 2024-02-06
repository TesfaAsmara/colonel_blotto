- wrote `blotto_jit.py` using numbah and joblib
- rewrote `slowest_blotto.py` code in C
    - Within that C code, after writing the first version, I refactored the
    read_strategies method to be included within the tournament method.
        - I also learned that in order to pass a 2D multidimensional array to a function
       in C, you must specify the number of entries for every dimension of that array, excluding the first dimension.
    - Notice that we cannot actually compute the max number of configurations.
      This is because the `long long` integer is not big enough for the expressions in the computation.
        - This limits us because now we cannot check the number of configurations read in from
          the file to the expected number of configurations within the C code. This can be overcome with a
          proof for the code.
- wrote Makefile
    - began writing documentation for Makefile in README.md
    - wrote command line interface for both python and C code
    - wrote Make command to record execution profiling metrics
        - wrote `plot_profiling.py` to extract, visualize the execution profiling metrics in `execution_times.png`,
           for the purpose of comparing the code

TODO:
    Estimate disk used for each folder in the results/ directory, get the average size of each file, get the median size of each file
    Ask for storage
    Have Youngsu double check C code