# Repo overview
In most recursion algorithms, the next recursive call is known. factorial(8) = 8 * factorial(7).
In [backtracking](https://en.wikipedia.org/wiki/Backtracking), the ***correct*** next recursive call
is not known. Each call is tentative. If the tentative call leads to a solution, great.
If not, the call is undone (backtracked), the argument updated, and another tentative recursive call
is done.

The ability of backtracking algorithms to try solutions that ultimately fail and continue on to
the next solution makes them ideal for puzzle solving. They tend to be extremely efficient because
each dead end prevents later recursive calls from being computed.

# Which problems are solved here?
* [Sudoku](https://en.wikipedia.org/wiki/Sudoku)
* [Knights Tour](https://en.wikipedia.org/wiki/Knight%27s_tour)
* [N Queens](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
* Pizza Hut pi day [challenge](https://blog.pizzahut.com/national-pi-day-math-problems-solved/)

# What does this library depend on?
* 'numpy'

