# Floyd-Warshall-Assignment

The `Floyd-Warshall-Assignment` repository hosts a recursive version of the Floyd-Warshall algorithm, aimed at determining the shortest paths within a directed graph with weights. Capable of processing both positive and negative edge weights, it provides reliable path calculations across varied graph structures, as long as there are no negative cycles present.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/liverpool-adhirs/Floyd-Warshall-Assignment.git
cd Floyd-Warshall-Assignment
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To use the recursive function, import it into your script, which will be in the floydwarshallcode folder.



```python
from floyd_recursive_code import floyd_warshall

#Using graph_6 as an input
from test_samples import graph_6

#Calling the recursive function with graph 6 as input.
floyd_warshall(graph_6)

```

## Running Unit Tests

Both the recursive and iterative algorithm reference the floydwarshallcode/test_samples.py file. You can use that file with the pre-made test cases or make changes to the test cases there.

To run the unit tests for the recursive code, you can use the below command in the terminal:

```bash
python -m unittest unittests/test_unit_recursive.py
```

To run the unit tests for the iterative code, you can use the below command in the terminal:

```bash
python -m unittest unittests/test_unit_imperative.py
```



## Running Performance Tests

To run the performance tests for the recursive code, you can edit the test cases in the test_performance_recursive.py file and use the below command in the terminal:
```bash
python .\performancetests\test_performance_recursive.py
```

To run the performance tests for the iterative code, you can edit the test cases in the test_performance_imperative.py file and use the below command in the terminal:
```bash
python .\performancetests\test_performance_imperative.py
```



## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Author

Adhir Soechit

## License

[MIT](https://choosealicense.com/licenses/mit/)
