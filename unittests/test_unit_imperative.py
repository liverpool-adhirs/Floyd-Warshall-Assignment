"""
This file performs the unit tests on the imperative algorithm.
Takes input and output from the test_samples file.
"""

import sys
import os
import unittest


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from floydwarshallcode.floyd_imperative_code import floyd_warshall
from floydwarshallcode.test_samples import (
    graph_3,graph_4,graph_5,graph_6,dense_graph_8,
    output_3,output_4,output_5,output_6,output_dense_8)


class TestImperative(unittest.TestCase):
    """
    This class contains tests which assess the functionality of the imperative algorithm.
    It utilises predefined input-output pairs from test_samples module.
    """
    def test_graph_3(self):
        """
        test_graph_3: Verifies algorithm output for a predefined graph scenario 'graph_3'.
        """
        self.assertEqual(floyd_warshall(graph_3),output_3,"This output is incorrect")

    def test_graph_4(self):
        """
        test_graph_4: Verifies algorithm output for a predefined graph scenario 'graph_4'.
        """
        self.assertEqual(floyd_warshall(graph_4),output_4,"This output is incorrect")

    def test_graph_5(self):
        """
        test_graph_5: Verifies algorithm output for a predefined graph scenario 'graph_5'.
        """
        self.assertEqual(floyd_warshall(graph_5),output_5,"This output is incorrect")

    def test_graph_6(self):
        """
        test_graph_6: Verifies algorithm output for a predefined graph scenario 'graph_6'.
        """
        self.assertEqual(floyd_warshall(graph_6),output_6,"This output is incorrect")

    def test_dense_graph_8(self):
        """
        test_dense_graph_8: Ensures accurate results for 'dense_graph_8', a dense graph example.
        """
        self.assertEqual(floyd_warshall(dense_graph_8),output_dense_8,"This output is incorrect")

if __name__=="__main__":
    unittest.main()
