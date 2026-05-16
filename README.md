This project wraps a CP-SAT solver to solve the set cover problem. Used for finding tetpc strict minimals.

Example: `py main_direct_ilp.py <fumen> <pattern> --output <output_file> --timeLimit <time_limit>`

`--output` specifies which file to write the final solutions to (one fumen per line). Omit this to not save the output. Regardless of what this is set to (or whether it is present) the output will be printed to stdout/console.

`--timeLimit` specifies how long to let the solver run. Omit this option to have no time limit. If the time limit is reached before the solver has finished, it will output the best solution it has found so far. Note that often this happens to be the optimal solution, because the solver takes time to prove that a given solution is actually optimal.

When reading the output of the CP-SAT solver, `next:[a,b]` means `a` is the best lower bound found for the size of the optimal solution, and the best solution found has size `b+1`.

`pip install -r requirements.txt` to install the solver library and other related dependencies.

You need to modify main_direct_ilp.py to change SFINDER_PATH and SFINDER_PREFIX according to what you type in the command line. Alternatively, supply a path.csv file directly to mirror_direct_ilp.py

There are likely methods to solve strict minimals faster, for example using holdless queues to make the problem matrix less dense (each solution covers a small amount of placement orders, which each cover a small amount of queues).

In previous versions, set cover was reduced to ILP, and an ILP solver (HiGHS) was used.
