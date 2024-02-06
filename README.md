Colonel Blotto
==============

This repository stores code for my math thesis on Colonel Blotto.

I will provide an introduction to the Colonel Blotto game soon.

I am interested in multiple directions:

    - It is important to note that the number of configurations increases drastically as 
    the number of trenches and the number of soldiers increase. This will take a large amount of time 
    to compute and storage to bookmark the results. Can we minimize and estimate the time and storage?
    - How can topological data analysis be utilized to reveal insightful strategies from datasets?
    - Can we quantify the information gain from the subset of games that we have been able to simulate?
    - We can represent the relationship between configurations utilizing a directed graph. 
    What methods can we apply to the graph?
    - I am concerned about the environmental impact of this research. A previous teammate named Jacob Wu 
    "How much does the temperature of the Earth increase when we send an email?" In that same manner,
    how much did my experiments increase the temperature of the Earth? How can we mitigate this?

You can follow along with my progress through the [notes](notes/) directory.

The files of importance are `slowest_blotto.py`, `blotto.jit.py`, `sums.c`, `blotto.c`, `Makefile`, and `plot_profiling.py`.
