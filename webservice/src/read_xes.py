import xmltodict
import json
import pandas as pd

COLUMN_NAMES = ["case", "event", "index", "date", "transition"]


def get_event_as_dict(case, index, event):
    """
    Extracts the important information for the event and converts them into a dictionary.
    The reason for the conversion is that it can easily be added to the trace-dataframe afterwards.

    Args:
        case (String): The name of the case to which the event belongs
        index (number): The index of the currect event in the case
        event (Dictionary): A dictionary consisting of the keys:
            string (Array): consiting of "org:resource", "concept:name" and "lifecycle:transition"
            date (date): timestamp of event

    Returns:
        Dictionary: A dictionary with the keys COLUMN_NAMES
    """
    event_name = list(filter(lambda p: p["@key"] == "concept:name", event["string"]))[0]["@value"] or ""
    lifecycleList = list(filter(lambda p: p["@key"] == "lifecycle:transition", event["string"]))
    transition = lifecycleList[0]["@value"] if len(lifecycleList) > 0 else "complete"
    return {
        "case": [case],
        "event": [event_name],
        "index": [index],
        "date": [event["date"]["@value"]],
        "transition": [transition],
    }


def get_trace_as_dataframe(trace):
    """
    Converts the given traces in a dataframe.
    A trace is one case which is provided in the file or respectively a sequence of events.

    Args:
        traces (Dictionary): A dictionary consisting of the keys:
            string (Object): showing name ("concept:name") of the trace
            event (Array): An array of events (-> get_event_as_dict)

    Returns:
        trace_df (Dataframe): A dataframe with the columns COLUMN_NAMES
    """
    trace_df = pd.DataFrame(columns=COLUMN_NAMES)

    # iteration through the events
    for index, event in enumerate(trace["event"]):
        case = trace["string"][0]["@value"] if type(trace["string"]) == list else trace["string"]["@value"]
        event_as_dict = get_event_as_dict(case, index, event)

        # an event is removed when it is not completed
        # an event-dictionary if converted into dataframe in order to add it to the trace-dataframe
        if event_as_dict["transition"][0] == "complete":
            event_as_df = pd.DataFrame.from_dict(event_as_dict)
            trace_df = pd.concat([trace_df, event_as_df], ignore_index=True)

    # reset index
    for index, row in trace_df.iterrows():
        row["index"] = index

    return trace_df


def get_dataframe_from_xes_file(file):
    """
    Converts a XES-file into a dataframe.

    Args:
        file (File): A file in the XES-format.
            for more information: https://fluxicon.com/blog/2010/09/intro-to-xes/

    Returns:
        df (Dataframe): A dataframe with the columns COLUMN_NAMES and a row for each event
    """
    # 1. step: read xes file
    xes_file = file.read()

    # 2. step: extract traces
    xes_dict = xmltodict.parse(xes_file)
    traces = xes_dict["log"]["trace"]

    # 3. step: create dataframe
    df = pd.DataFrame(columns=COLUMN_NAMES)

    for trace in traces:
        trace_df = get_trace_as_dataframe(trace)
        df = pd.concat([df, trace_df])

    return df