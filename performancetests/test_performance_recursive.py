"""
This code tests the performance for the recursive code.

"""
import sys
import os
import cProfile



SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from floydwarshallcode.floyd_recursive_code import floyd_warshall
from floydwarshallcode.test_samples import graph_6

#Performance testing using graph_6 as input.
cProfile.run("floyd_warshall(graph_6)")
