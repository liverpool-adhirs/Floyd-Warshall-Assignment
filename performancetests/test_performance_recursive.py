"""
This code tests the performance for the recursive code.

"""
import sys
import os
import cProfile
import pstats


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from floydwarshallcode.floyd_recursive_code import floyd_warshall
from floydwarshallcode.test_samples import graph_6


if __name__ == "__main__":
    with cProfile.Profile() as profile:
        floyd_warshall(graph_6)
    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats()
