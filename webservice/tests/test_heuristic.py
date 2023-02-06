import pytest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
import copy

import sys

sys.path.append("..")

from webservice.src.heuristic_algorithm import *

from webservice.tests.example_data_heuristic import *

event0 = copy.deepcopy(event0_reduced)
event1 = copy.deepcopy(event1_reduced)
event2 = copy.deepcopy(event2_reduced)
event4 = copy.deepcopy(event4_reduced)

def initialize_dataframe():
    """
    Initialized dataframe by 
        - concating the (right) number of occurences of each trace
        - converting directory of each trace to dataframe
        - and concating all traces
    in order to create example on p. 202
    """
    for i in list(range(1, 10)):
        if i < 5:
            event0["case"] += ['a{}'.format(i), 'a{}'.format(i)]
            event0["index"] += event0_reduced["index"]
            event0["event"] += event0_reduced["event"]

        event1["case"] += ['b{}'.format(i), 'b{}'.format(i), 'b{}'.format(i), 'b{}'.format(i)]
        event1["index"] += event1_reduced["index"]
        event1["event"] += event1_reduced["event"]

        event2["case"] += ['c{}'.format(i), 'c{}'.format(i), 'c{}'.format(i), 'c{}'.format(i)]
        event2["index"] += event2_reduced["index"]
        event2["event"] += event2_reduced["event"]

        event4["case"] += ['e{}'.format(i), 'e{}'.format(i), 'e{}'.format(i)]
        event4["index"] += event4_reduced["index"]
        event4["event"] += event4_reduced["event"]

    event0_df = pd.DataFrame(event0)
    event1_df = pd.DataFrame(event1)
    event0_df = pd.concat([event0_df, event1_df])
    event2_df = pd.DataFrame(event2)
    event0_df = pd.concat([event0_df, event2_df])
    event3_df = pd.DataFrame(event3)
    event0_df = pd.concat([event0_df, event3_df])
    event4_df = pd.DataFrame(event4)
    event0_df = pd.concat([event0_df, event4_df])
    event5_df = pd.DataFrame(event5)
    event_df = pd.concat([event0_df, event5_df])
    return event_df


frequency_matrix_solution_df = pd.DataFrame(frequency_matrix_solution)
frequency_matrix_solution_df.index = frequency_matrix_solution_df.columns
dependency_matrix_solution_df = pd.DataFrame(dependency_matrix_solution)
dependency_matrix_solution_df.index = dependency_matrix_solution_df.columns

frequency_matrix_solution_df2 = pd.DataFrame(frequency_matrix_solution2)
frequency_matrix_solution_df2.index = frequency_matrix_solution_df2.columns
dependency_matrix_solution_df2 = pd.DataFrame(dependency_matrix_solution2)
dependency_matrix_solution_df2.index = dependency_matrix_solution_df2.columns


def test_get_frequency_matrix():
    """
    Testing the fourth step of the Heuristic Miner:
    get_frequency_matrix()
    """
    event_df = initialize_dataframe()
    frequency_matrix = get_frequency_matrix(event_df)
    assert_frame_equal(frequency_matrix, frequency_matrix_solution_df)

    df2 = pd.DataFrame(data2)
    frequency_matrix2 = get_frequency_matrix(df2)
    assert_frame_equal(frequency_matrix2, frequency_matrix_solution_df2)


def test_get_dependency_matrix():
    """
    Testing the fifth step of the Heuristic Miner:
    get_dependency_matrix()
    """
    dependency_matrix = get_dependency_matrix(frequency_matrix_solution_df)
    # round floats to two decimal number
    dependency_matrix = dependency_matrix.round(2)
    assert_frame_equal(dependency_matrix, dependency_matrix_solution_df)

    dependency_matrix2 = get_dependency_matrix(frequency_matrix_solution_df2)
    # round floats to two decimal number
    dependency_matrix2 = dependency_matrix2.round(2)
    assert_frame_equal(dependency_matrix2, dependency_matrix_solution_df2)

def test_filter_edges():
    """
    Testing the sixth and seventh step of the Heuristic Miner:
    get_edges() and filter_edges()
    """
    edges0 = get_edges(frequency_matrix_solution_df, dependency_matrix_solution_df)
    edges0 = filter_edges(edges0, min_edge0, dep_thresh0)
    assert np.array_equal(sorted(edges0_solution), sorted(edges0))

    edges1 = get_edges(frequency_matrix_solution_df, dependency_matrix_solution_df)
    edges1 = filter_edges(edges1, min_edge1, dep_thresh1)
    assert np.array_equal(sorted(edges1_solution), sorted(edges1))


    edges2 = get_edges(frequency_matrix_solution_df2, dependency_matrix_solution_df2)
    edges2 = filter_edges(edges2, min_edge2, dep_thresh2)
    assert np.array_equal(sorted(edges2_solution), sorted(edges2))

    edges3 = get_edges(frequency_matrix_solution_df2, dependency_matrix_solution_df2)
    edges3 = filter_edges(edges3, min_edge3, dep_thresh3)
    assert np.array_equal(sorted(edges3_solution), sorted(edges3))


