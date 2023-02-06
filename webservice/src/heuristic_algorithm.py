import pandas as pd
import numpy as np
from enum import Enum

from webservice.src.utils import *

def get_frequency_matrix(event_df):
    """
    Returns the frequency matrix of a given event-dataframe.
    The frequency is the number of "directly follows" relations between two events.

    Args:
        event_df (Dataframe): A dataframe consisting of the columns ["case" (String), "index" (number), "event" (String)]

    Returns:
        matrix (Dataframe): A dataframe displaying the frequency matrix
    """
    transition_names = get_all_activities(event_df)
    matrix = pd.DataFrame(index=transition_names, columns=transition_names).fillna(0)

    for from_activity in transition_names:
        for to_activity in transition_names:
            matrix[to_activity][from_activity] = get_number_of_directly_followed(event_df, from_activity, to_activity)
    
    return matrix


def get_dependency_matrix(frequency_matrix):
    """
    Returns the dependency matrix generated through the frequency matrix.
    Functions from p. 202

    Args:
        frequency_matrix (Dataframe): A dataframe displaying the frequency matrix

    Returns:
        dependency_matrix (Dataframe): A dataframe showing the dependency matrix
    """
    dependency_matrix = pd.DataFrame(index=list(frequency_matrix.columns), columns=list(frequency_matrix.columns)).fillna(0)
    
    for from_activity in list(frequency_matrix.columns):
        for to_activity in list(frequency_matrix.columns):
            if from_activity != to_activity:
                dependency = (abs(frequency_matrix[to_activity][from_activity]) - abs(frequency_matrix[from_activity][to_activity])) / \
                    (abs(frequency_matrix[to_activity][from_activity]) + abs(frequency_matrix[from_activity][to_activity]) + 1)
                dependency_matrix.loc[from_activity, to_activity] = dependency
            else:
                dependency = abs(frequency_matrix[to_activity][from_activity]) / (abs(frequency_matrix[to_activity][from_activity]) + 1)
                dependency_matrix.loc[from_activity, to_activity] = dependency

    return dependency_matrix


def get_edges(frequency_matrix, dependency_matrix):
    """
    Returns an array of edges combined with corresponding frequency and dependency values.

    Args:
        frequency_matrix (Dataframe): A dataframe showing the frequency-matrix
        dependency_matrix (Dataframe): A dataframe showing the  dependency-matrix

    Returns:
        pairs (Array of Tupels): An array of pairs of activities with the affiliated frequency and dependency
    
    Example: Relation: A -> B => Array-Element: (A, B, Frequency, Dependency)
    """
    pairs = []

    for column in list(frequency_matrix.columns):
        for row in list(frequency_matrix.index):
            frequency = frequency_matrix[column][row]
            dependency = dependency_matrix[column][row]
            pairs.append((row, column, frequency, dependency))

    return pairs

def filter_edges(edges, min_edge, dep_threshold):
    """
    Filters the edges by the minimum number of edges (frequency) and minimum dependency threshold

    Args:
        pairs (Array of Tupels): An array of pairs of activities with the affiliated frequency and dependency
            (String, string, number, number)
        min_edge (number): Minimum number of edges
        dep_threshold (number): Minimum dependency threshold

    Returns:
        Array of Tupels: An array of pairs of activities with the affiliated frequency and dependency
            (string, string, string, string)
    """
    filtered_edge = list(filter(lambda p: float(p[2]) >= float(min_edge) and float(p[3]) >= float(dep_threshold), edges))
    return list(map(lambda p: (p[0], p[1], str(round(p[2], 2)), str(round(p[3], 2))), filtered_edge))


def run_heuristic_algorithm(event_df, dep_threshold, min_edge):
    """
    This function runs the Heuristic Miner based on 
    https://ebookcentral.proquest.com/lib/munchentech/detail.action?docID=4505537

    Args:
        event_df (Dataframe): A dataframe with the columns COLUMN_NAMES and a row for each event

    Returns:
        place_names (Array): An array of the event/activities-names (nodes of the dependency-net)
        filtered_edge (Array): An array of edges (of the dependency-net) including the starting and ending activities,
            the frequency and the dependency as (string, string, string, string)
    """

    # step 1: transitions in event log
    place_names = get_all_activities(event_df)

    # step 2: initial element of traces
    initial_elements = get_trace_starts(event_df)

    # step 3: final element of traces
    final_elements = get_trace_ends(event_df)

    # step 4: frequency matrix
    frequency_matrix = get_frequency_matrix(event_df)

    # step 5: dependency matrix
    dependency_matrix = get_dependency_matrix(frequency_matrix)

    # step 6: pairs of casuality-related activities
    edges = get_edges(frequency_matrix, dependency_matrix)

    # step 7: filter the pairs by frequency and dependency and convert numbers to string
    filtered_edges = filter_edges(edges, min_edge, dep_threshold)

    for initial_element in initial_elements:
        frequency = event_df.groupby(["case"]).apply(lambda a: a[(a["index"] == 0) & (a["event"] == initial_element)]).shape[0]
        dependency = frequency / (frequency + 1)
        filtered_edges.append(("iL", initial_element, frequency, round(dependency, 2)))

    for final_element in final_elements:
        frequency = event_df.groupby(["case"]).apply(lambda a: a[(a["index"] == a["index"].max()) & (a["event"] == final_element)]).shape[0]
        dependency = frequency / (frequency + 1)
        filtered_edges.append((final_element, "oL", frequency, round(dependency, 2)))

    return place_names, filtered_edges, frequency_matrix, dependency_matrix.round(2)
