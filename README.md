wraps an ILP solver to solve set cover for tetpc strict minimals

set timelimit to limit how long the solver runs. on timeout it will return the best solution it has found. note that it often finds the optimal solution long before proving that it is the optimal solution, so you are likely to get an optimal/near-optimal solution

`py main_direct_ilp <fumen> <pattern> --output <output_file> --timeLimit <time_limit>`

omit output to not save output to a file (note that the answer is always printed to stdout/console)

omit time limit to have no time limit

requires pulp library

note that this likely can be sped up (SAT solvers and ILP solvers usually solve problems of these sizes faster?) but i have no time to check right now.

you need to modify main_direct_ilp.py to change SFINDER_PATH and SFINDER_PREFIX according to what you type in the command line ! alternatively, supply a path.csv file directly to mirror_direct_ilp.py