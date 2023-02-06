import numpy as np


def get_all_activities(event_df):
    """
    Returns all activities.

    Args:
        event_df (Dataframe): A dataframe consisting of the columns ["case" (String), "index" (number), "event" (String)]

    Returns:
        Array (String): An array of the names of all activities
    """
    return np.sort(event_df["event"].unique())


def get_trace_starts(event_df):
    """
    Returns the starting activities of the traces.

    Args:
        event_df (Dataframe): A dataframe consisting of the columns ["case" (String), "index" (number), "event" (String)]

    Returns:
        Array (String): An array of activities the traces start with
    """
    return (
        event_df.groupby(["case"]).apply(lambda a: a[a["index"] == 0])["event"].unique()
    )


def get_trace_ends(event_df):
    """
    Returns the end activities of the traces.

    Args:
        event_df (Dataframe): A dataframe consisting of the columns ["case" (String), "index" (number), "event" (String)]

    Returns:
        Array (String): An array of activities the traces end with
    """
    return (
        event_df.groupby(["case"])
        .apply(lambda a: a[a["index"] == a["index"].max()])["event"]
        .unique()
    )


def get_number_of_directly_followed_in_case(case_df, from_activity, to_activity):
    """
    Returns the number of occurences the second activity directly follows the first transition for the given case.

    Args:
        case_df (Dataframe): A dataframe consisting of the columns ["case" (String), "index" (number), "event" (String)]
            All events have the same case.
        from_activity (String): The name of the first activity
        to_activity (String): The name of the second activity

    Returns:
        occ (number): Occurences the second activity directly follows the first transition for the given case
    """
    filtered_events = case_df[
        (case_df["event"] == from_activity) | (case_df["event"] == to_activity)
    ]

    occ = 0
    if len(filtered_events["event"]) < 2:
        return occ

    from_activity_indexes = filtered_events[filtered_events["event"] == from_activity]["index"]
    to_activity_indexes = filtered_events[filtered_events["event"] == to_activity]["index"]

    for from_index in from_activity_indexes.values:
        if from_index + 1 in to_activity_indexes.values:
            occ += 1

    return occ


def get_number_of_directly_followed(event_df, from_activity, to_activity):
    """
    Returns number of occurences when the second activity directly follows the first activity (for all traces).

    Args:
        event_df (Dataframe): A dataframe consisting of the columns ["case" (String), "index" (number), "event" (String)]
        from_activity (String): The name of the first activity
        to_activity (String): The name of the second activity

    Returns:
        Number: Number of times when the second activity directly follows the first activity
    """
    directly_followed_per_case = (
        event_df.groupby(["case"])
        .apply(
            lambda df: get_number_of_directly_followed_in_case(df, from_activity, to_activity)
        )
        .reset_index()
    )
    series_as_array = directly_followed_per_case[0].values
    return sum(series_as_array)
