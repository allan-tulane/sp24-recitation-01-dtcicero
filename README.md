# CMPS 2200  Recitation 01

**Name (Team Member 1):** Daniel Cicero  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`. All tests are in `test_main.py`.

## Install Python Dependency

We need Python library of "tabulate" to visualize the results in a good shape. Please install it by running 'pip install tabulate' or 'pip install -r requirements.txt' in Shell Tab of Repl.  

## Running and testing your code

- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [ ] 2. Test that your function is correct by calling from the command-line `pytest test_main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 

**TODO: your answer goes here**
The worst case input of 'key' for 'linear_search' is when 'key' is the last value in the list, or not in the list at all. This is because such a 'key' forces 'linear_search' to iterate through its entire list to find said 'key', exhausting the maximum amount of time and memory resources. The worst case input of 'key' for 'binary_search' is a 'key' that is both not present in the list, and either smaller than the smallest key in the list or larger than the largest. This is because such a key forces the 'binary_search' to continuously divide in half indefinitely until it is determined the key is outside the range of the list, forcing the maximum number of operations. 

- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`? 

**TODO: your answer goes here**
The best case input value of 'key' for linear search is if 'key' is equal to the key at the 0 position of the list, or the first key in the list. This is because this is the key that linear search will check first, allowing it to complete its search in only one move, which is best case. The best case input value of 'key' for binary search is if 'key' is equal to the key in the middle of the given list. This is because the first job of 'binary_search' is to identify the middle of a given input list, and immediately check that middle value against the desired 'key'. Should 'key' be equal to this middle value, it allows for the least possible operations, or best case for this function. 

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.
      

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest test_main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:

**TODO: add your timing results here**

|        n |   linear |   binary |
|----------|----------|----------|
|       10 |    0.006 |    0.009 |
|      100 |    0.008 |    0.005 |
|     1000 |    0.078 |    0.008 |
|    10000 |    0.850 |    0.010 |
|   100000 |    5.537 |    0.036 |
|  1000000 |   98.309 |    0.036 |
| 10000000 | 1215.871 |    0.047 |

- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

**TODO: your answer goes here**
These do match my theoretical results, because the results show linear search growing linearly with the size of the input, while binary search grows at a much slower rate proportional to $O(log_2(n))$.

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times. 
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? **TODO: your answer goes here**
      + Using linear search, worst-case complexity is k * O(n), or O(kn)
  + For binary search? **TODO: your answer goes here** Using binary search, sorting the list takes Theta(n^2) time, binary search takes O(log(n)), and together the worst-case complexity is Theta(n^2) + k * O(log(n)), which simplified is Theta(n^2 + klog(n))
    
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? **TODO: your answer goes here** 
For values of 'n' such that Θ(n^2 +klogn)<O(kn), it is more efficient to first sort and then use binary search, as the threshold is crossed such that it is more efficient to first sort the list and then perform binary search.