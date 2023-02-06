import pandas as pd
import numpy as np
from enum import Enum

from webservice.src.utils import *


class Relation(str, Enum):
    """
    Enum describing the relation between two events:
        - causality right (->)
        - causality light (<-)
        - parallelity (||)
        - unrelated/indepedent (#)
    """
    causality_right = "causality_right"
    causality_left = "causality_left"
    parallel = "parallel"
    unrelated = "unrelated"


def set_location_in_matrix(matrix, from_activity, to_activity, event_df):
    """
    Sets the relation in the location [from_activity, to_activity] of the given footprint matrix.

    Args:
        matrix (Dataframe): A dataframe of the current footprint-matrix
        from_activity (String): The name of the row to set the relation
        to_activity (String): The name of the column to set the relation
        event_df (Dataframe): A dataframe consisting of the columns ["case" (String), "index" (number), "event" (String)]
    """

    # number of occurrences when the first activity is followed by the second activity
    directly_followed = get_number_of_directly_followed(
        event_df, from_activity, to_activity
    )

    # number of occurrences when the second activity is followed by the first activity
    reversed_directly_followed = get_number_of_directly_followed(
        event_df, to_activity, from_activity
    )

    # sets the relation of type Relation (Enum)
    if directly_followed > 0 and reversed_directly_followed > 0:
        matrix[to_activity][from_activity] = Relation.parallel

    if directly_followed > 0 and reversed_directly_followed == 0:
        matrix[to_activity][from_activity] = Relation.causality_right

    if directly_followed == 0 and reversed_directly_followed > 0:
        matrix[to_activity][from_activity] = Relation.causality_left

    if directly_followed == 0 and reversed_directly_followed == 0:
        matrix[to_activity][from_activity] = Relation.unrelated


def get_footprint_matrix(event_df):
    """
    Returns the footprint matrix of a given event-dataframe.

    Args:
        event_df (Dataframe): A dataframe consisting of the columns ["case" (String), "index" (number), "event" (String)]

    Returns:
        matrix (Dataframe): A dataframe showing the footprint-matrix with the cell-type Relation (Enum)
    """
    transition_names = get_all_activities(event_df)
    matrix = pd.DataFrame(index=transition_names, columns=transition_names).fillna(Relation.unrelated)
    
    for from_activity in transition_names:
        for to_activity in transition_names:
            set_location_in_matrix(matrix, from_activity, to_activity, event_df)
    
    return matrix


def is_unrelated(footprint_matrix, list, element):
    """
    Returns whether all elements in the list are unrelated to the element.

    Args:
        footprint_matrix (Dataframe): A dataframe showing the footprint-matrix with the cell-type Relation (Enum)
        list (Array): An array of activity-names
        element (string): Name of a single activity

    Returns:
        Boolean: shows whether the single element is unrelated to every activity of the list
    """
    for list_element in list:
        if footprint_matrix[list_element][element] != Relation.unrelated:
            return False
    return True


def create_maximal_pairs(footprint_matrix):
    """
    Creates the maximal pairs based on the footprint matrix.

    Args:
        footprint_matrix (Dataframe): A dataframe showing a footprint-matrix

    Returns:
        maximale_pairs (Array of Tupels): Each Tupel contains two arrays of activities.
            The pairs are showing the causality between each element of the first array and each element of the second array.
            The elements in each array are unrelated.
    """
    # extract pairs of element which are have a causal relation
    pairs = []
    for column in list(footprint_matrix.columns):
        for row in list(footprint_matrix.index):
            relation = footprint_matrix[column][row]
            if relation == Relation.causality_right:
                pairs.append((row, column))

    maximal_pairs = list(map(lambda pair: ([pair[0]], [pair[1]]), pairs))

    # iteration through all pairs:
    # when it is possible (condition above) the current pair is added to the maximal pair
    # by duplicating the maximal pair and adding either the first or second acticity to the maximal pair.
    # The duplication is necessary because a pair can occur more than one time.
    # Example: A -> B ; A -> C ; A -> D with B # C ; B # D and C -> D
    #          => A -> (B, C) and A -> (B, D)

    for pair in pairs:
        pairs_to_be_added = []
        for maximal_pair in maximal_pairs:
            if pair[0] in maximal_pair[0] and pair[1] not in maximal_pair[1]:
                if is_unrelated(footprint_matrix, maximal_pair[1], pair[1]):
                    pairs_to_be_added.append(([pair[0]], [pair[1]]))
                    maximal_pair[1].append(pair[1])

            if pair[1] in maximal_pair[1] and pair[0] not in maximal_pair[0]:
                if is_unrelated(footprint_matrix, maximal_pair[0], pair[0]):
                    pairs_to_be_added.append(([pair[0]], [pair[1]]))
                    maximal_pair[0].append(pair[0])
        maximal_pairs += pairs_to_be_added

    # Activities which are in a parallel relation with itself can not be connected to other activities
    def remove_transition(pair, transition):
        if transition in pair[0]: 
            pair[0].remove(transition)
        if transition in pair[1]: 
            pair[1].remove(transition)
        return pair

    # Remove the parallel element from each pair
    # If a pair is now empty, it is deleted.
    for transition in list(footprint_matrix.columns):
        if footprint_matrix[transition][transition] is Relation.parallel:
            maximal_pairs = list(map(lambda pair: remove_transition(pair, transition), maximal_pairs))
            maximal_pairs = list(filter( lambda pair: len(pair[0]) > 0 and len(pair[1]), maximal_pairs))

    return maximal_pairs


def reduce_maximal_pairs(maximal_pairs):
    """
    Reduces the maximal pairs. If a pair is included in another one, the shorter pair is removed.
    Example: (A -> (B, C)) and (A -> B) ==> (A -> (B, C))

    Args:
        maximal_pairs (Array of Tupels): An array of tuples showing the maximal pairs

    Returns:
        reduced_array (Array of Tupels): Each Tupel contains two arrays of activities.
    """
    reduced_array = []
    for pair in maximal_pairs:
        if len(list(filter(lambda reduced_pair: set(pair[0]).issubset(reduced_pair[0]) and set(pair[1]).issubset(reduced_pair[1]), reduced_array))) > 0:
                continue
        elif len(list(filter(lambda reduced_pair: set(reduced_pair[0]).issubset(pair[0]) and set(reduced_pair[1]).issubset(pair[1]), reduced_array))) > 0:
            pairs_to_be_removed = list(filter(lambda reduced_pair: set(reduced_pair[0]).issubset(pair[0]) and set(reduced_pair[1]).issubset(pair[1]), reduced_array))
            for pair_to_be_removed in pairs_to_be_removed:
                reduced_array.remove(pair_to_be_removed)
            reduced_array.append(pair)
        else:
            reduced_array.append(pair)
    return reduced_array


def run_alpha_algorithm(event_df):
    """
    This function runs the Alpha Miner based on 
    https://ebookcentral.proquest.com/lib/munchentech/detail.action?docID=4505537

    Args:
        event_df (Dataframe): A dataframe with the columns COLUMN_NAMES and a row for each event

    Returns:
        activity_names (Array): An array the activity (respectively event) names (activity-nodes of the petrinet)
        P_L (Array): An array of the transitions between the activities (transition-nodes of the petrinet)
        F_L (Array): An array of flows which will be the edges of the petrinet
    """
    # step 1: transitions in event log (T_L)
    activity_names = get_all_activities(event_df)

    # step 2: initial element of traces (T_I)
    initial_elements = get_trace_starts(event_df)

    # step 3: final element of traces (T_O)
    final_elements = get_trace_ends(event_df)

    # step 4: footprint matix
    footprint_matrix = get_footprint_matrix(event_df)

    # step 5: maximal pairs of casuality-related activities (Y_L)
    Y_L = create_maximal_pairs(footprint_matrix)
    Y_L = reduce_maximal_pairs(Y_L)

    # step 6: determine transition-nodes (P_L)
    P_L = Y_L.copy()
    P_L.append("iL")
    P_L.append("oL")

    # step 7: determine edges between activity and transitions (F_L)
    F_L = []
    for pair in Y_L:
        for from_activity in pair[0]:
            F_L.append((from_activity, pair))
        for to_activity in pair[1]:
            F_L.append((pair, to_activity))

    for start in initial_elements:
        F_L.append(("iL", start))

    for end in final_elements:
        F_L.append((end, "oL"))

    return activity_names, P_L, F_L, footprint_matrix