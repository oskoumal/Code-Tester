# Code-Tester-script
Joern - based python script program for searching bugs in C/C++ code using graph database queries

Simple script program for hunting of vulnerabilities using number of graph database queries

usage: Run.py [-h] [-o {1,2,3,4,5,6}] [-l LIMIT]

Run withount arguments for interactive program menu and additional info.

optional arguments:
  -h, --help            show this help message and exit
  -o {1,2,3,4,5,6}, --option {1,2,3,4,5,6}
			                  Options: 1) Run all Buffer Overflow tests 2) Run all
                        Memory Disclosure tests 3) Run all Null Pointer
                        Dereference tests 4) Run all tests 5) Settings 6) Help
  -l LIMIT, --limit LIMIT
                        maximum execution time of query in minutes


example:

python Run.py -o 2 -l 1
