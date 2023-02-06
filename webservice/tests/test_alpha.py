import pytest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal

import sys

sys.path.append("..")

from webservice.src.alpha_algorithm import *

# from webservice.src.alpha_algorithm import get_trace_starts
# from webservice.src.alpha_algorithm import get_trace_ends
# from webservice.src.alpha_algorithm import get_footprint_matrix
# from webservice.src.alpha_algorithm import get_causality_pairs
# from webservice.src.alpha_algorithm import create_maximal_pairs
# from webservice.src.alpha_algorithm import run_alpha_algorithm
# from webservice.src.alpha_algorithm import Relation

from webservice.tests.example_data_alpha import *

# convert event-logs (directories) to dataframes
df0 = pd.DataFrame(data0)
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

# convert the solution of footprint-matrices to dataframes
footprint0_solution_df = pd.DataFrame(footprint0_solution)
footprint0_solution_df.index = all_relations0_solution

footprint1_solution_df = pd.DataFrame(footprint1_solution)
footprint1_solution_df.index = all_relations1_solution

footprint3_solution_df = pd.DataFrame(footprint3_solution)
footprint3_solution_df.index = all_relations3_solution


def test_get_all_activities():
    """
    Testing the first step of the Alpha Miner:
    get_all_activities()
    """
    all_relations0 = get_all_activities(df0)
    assert np.array_equal(all_relations0_solution, all_relations0)

    all_relations1 = get_all_activities(df1)
    assert np.array_equal(all_relations1_solution, all_relations1)

    all_relations2 = get_all_activities(df2)
    assert np.array_equal(all_relations2_solution, all_relations2)

    all_relations3 = get_all_activities(df3)
    assert np.array_equal(all_relations3_solution, all_relations3)


def test_get_trace_start():
    """
    Testing the second step of the Alpha Miner:
    get_trace_start()
    """
    assert np.array_equal(get_trace_starts(df0), ["A"])

    assert np.array_equal(get_trace_starts(df1), ["A"])

    assert np.array_equal(get_trace_starts(df2), ["A", "B"])

    assert np.array_equal(get_trace_starts(df3), ["A"])


def test_get_trace_ends():
    """
    Testing the third step of the Alpha Miner:
    get_trace_start()
    """
    assert np.array_equal(get_trace_ends(df0), ["D"])

    assert np.array_equal(get_trace_ends(df1), ["G"])

    assert np.array_equal(get_trace_ends(df2), ["D", "E"])

    assert np.array_equal(get_trace_ends(df3), ["F"])


def test_get_footprint_matrix():
    """
    Testing the fourth step of the Alpha Miner:
    get_footprint_matrix()
    """
    footprint0 = get_footprint_matrix(df0)
    assert_frame_equal(footprint0, footprint0_solution_df)

    footprint1 = get_footprint_matrix(df1)
    assert_frame_equal(footprint1, footprint1_solution_df)

    footprint3 = get_footprint_matrix(df3)
    assert_frame_equal(footprint3, footprint3_solution_df)


def test_create_maximal_pairs():
    """
    Testing the fifth step of the Alpha Miner:
    create_maximal_pairs() and reduce_maximal_pairs()
    """
    maximal_pairs0 = create_maximal_pairs(footprint0_solution_df)
    maximal_pairs0 = reduce_maximal_pairs(maximal_pairs0)
    assert np.array_equal(sorted(maximal_pairs0_solution), sorted(maximal_pairs0))

    maximal_pairs1 = create_maximal_pairs(footprint1_solution_df)
    maximal_pairs1 = reduce_maximal_pairs(maximal_pairs1)
    assert np.array_equal(sorted(maximal_pairs1_solution), sorted(maximal_pairs1))

    maximal_pairs3 = create_maximal_pairs(footprint3_solution_df)
    maximal_pairs3 = reduce_maximal_pairs(maximal_pairs3)
    assert np.array_equal(sorted(maximal_pairs3_solution), sorted(maximal_pairs3))
