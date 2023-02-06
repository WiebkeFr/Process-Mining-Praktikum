import sys
sys.path.append("..")

from webservice.src.alpha_algorithm import Relation

# EXAMPLE_DATA 1 (from L_1) from page 167 [1]
data0 = {
        "case": ["c0", "c0", "c0", "c0",
                 "c1", "c1", "c1", "c1",
                 "c2", "c2", "c2"],
        "index": [0, 1, 2, 3, 
                  0, 1, 2, 3,
                  0, 1, 2],
        "event": ["A", "B", "C", "D",
                  "A", "C", "B", "D",
                  "A", "E", "D"]
}

all_relations0_solution = ["A", "B", "C", "D", "E"]

causality_pairs0_solution = [("A", "B"), ("A", "C"), ("A", "E"), ("B", "D"), ("C", "D"), ("E", "D")]

maximal_pairs0_solution = [(["A"], ["B", "E"]), (["A"], ["C", "E"]), (["B", "E"], ["D"]), (["C", "E"], ["D"])]

footprint0_solution = {
    "A": [Relation.unrelated, Relation.causality_left, Relation.causality_left, Relation.unrelated, Relation.causality_left],
    "B": [Relation.causality_right, Relation.unrelated, Relation.parallel, Relation.causality_left, Relation.unrelated],
    "C": [Relation.causality_right,  Relation.parallel, Relation.unrelated, Relation.causality_left, Relation.unrelated],
    "D": [Relation.unrelated, Relation.causality_right, Relation.causality_right, Relation.unrelated, Relation.causality_right],
    "E": [Relation.causality_right, Relation.unrelated, Relation.unrelated, Relation.causality_left,  Relation.unrelated]
}

# EXAMPLE 3 (from L_3) [1]
data1 = {
        "case": ["c0", "c0", "c0", "c0", "c0", "c0", "c0", "c0", "c0", "c0", "c0", 
                 "c1", "c1", "c1", "c1", "c1", "c1",
                 "c2", "c2", "c2", "c2", "c2", "c2", "c2", "c2", "c2", "c2", "c2", "c2", "c2", "c2", "c2", "c2"],
        "index": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                  0, 1, 2, 3, 4, 5,
                  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "event": ["A", "B", "C", "D", "E", "F", "B", "D", "C", "E", "G",
                  "A", "B", "D", "C", "E", "G", 
                  "A", "B", "C", "D", "E", "F", "B", "C", "D", "E", "F", "B", "D", "C", "E", "G"]
}

all_relations1_solution = ["A", "B", "C", "D", "E", "F", "G"]

causality_pairs1_solution = [("A", "B"), ("B", "C"), ("B", "D"), ("C", "E"), ("D", "E"), ("E", "F"), ("E", "G"), ("F", "B")]

maximal_pairs1_solution = [(["A", "F"], ["B"]), (["B"], ["C"]), (["B"], ["D"]), (["C"], ["E"]), (["D"], ["E"]), (["E"], ["F", "G"])]

footprint1_solution = {
    "A": [Relation.unrelated, Relation.causality_left, Relation.unrelated, Relation.unrelated, Relation.unrelated, Relation.unrelated, Relation.unrelated],
    "B": [Relation.causality_right, Relation.unrelated, Relation.causality_left, Relation.causality_left, Relation.unrelated, Relation.causality_right, Relation.unrelated],
    "C": [Relation.unrelated, Relation.causality_right, Relation.unrelated, Relation.parallel, Relation.causality_left, Relation.unrelated, Relation.unrelated],
    "D": [Relation.unrelated, Relation.causality_right, Relation.parallel, Relation.unrelated, Relation.causality_left, Relation.unrelated, Relation.unrelated],
    "E": [Relation.unrelated, Relation.unrelated, Relation.causality_right, Relation.causality_right, Relation.unrelated, Relation.causality_left, Relation.causality_left],
    "F": [Relation.unrelated, Relation.causality_left, Relation.unrelated, Relation.unrelated, Relation.causality_right, Relation.unrelated, Relation.unrelated],
    "G": [Relation.unrelated, Relation.unrelated, Relation.unrelated, Relation.unrelated, Relation.causality_right, Relation.unrelated, Relation.unrelated]
}

# EXAMPLE_DATA 1 (from L_4) [1]
data2 = {
        "case": ["c0", "c0", "c0", 
                 "c1", "c1", "c1",
                 "c2", "c2", "c2",
                 "c3", "c3", "c3"],
        "index": [0, 1, 2,  
                  0, 1, 2, 
                  0, 1, 2,
                  0, 1, 2],
        "event": ["A", "C", "D",
                  "B", "C", "D",
                  "A", "C", "E",
                  "B", "C", "E"]
}

all_relations2_solution = ["A", "B", "C", "D", "E"]

causality_pairs2_solution = [("A", "C"), ("B", "C"), ("C", "D"), ("C", "E")]


# EXAMPLE_DATA 3 (from L_5) [1]
data3 = {
        "case": ["c0", "c0", "c0", "c0", 
                 "c1", "c1", "c1", "c1", "c1", "c1", "c1",
                 "c2", "c2", "c2", "c2", "c2", "c2", "c2",
                 "c3", "c3", "c3", "c3", "c3", "c3", "c3",
                 "c4", "c4", "c4", "c4", "c4", "c4", "c4"],
        "index": [0, 1, 2, 3, 
                  0, 1, 2, 3, 4, 5, 6,
                  0, 1, 2, 3, 4, 5, 6,
                  0, 1, 2, 3, 4, 5, 6,
                  0, 1, 2, 3, 4, 5, 6],
        "event": ["A", "B", "E", "F", 
                  "A", "B", "E", "C", "D", "B", "F",
                  "A", "B", "C", "E", "D", "B", "F",
                  "A", "B", "C", "D", "E", "B", "F",
                  "A", "E", "B", "C", "D", "B", "F",]
}

all_relations3_solution = ["A", "B", "C", "D", "E", "F"]

causality_pairs3_solution = [("A", "B"), ("A", "E"), ("B", "C"), ("B", "F"), ("C", "D"), ("D", "B"), ("E", "F")]

maximal_pairs3_solution = [(["A", "D"], ["B"]), (["A"], ["E"]), (["B"], ["C", "F"]), (["E"], ["F"]), (["C"], ["D"])]

footprint3_solution = {
    "A": [Relation.unrelated, Relation.causality_left, Relation.unrelated, Relation.unrelated, Relation.causality_left, Relation.unrelated],
    "B": [Relation.causality_right, Relation.unrelated, Relation.causality_left, Relation.causality_right, Relation.parallel, Relation.causality_left],
    "C": [Relation.unrelated, Relation.causality_right, Relation.unrelated, Relation.causality_left, Relation.parallel, Relation.unrelated],
    "D": [Relation.unrelated, Relation.causality_left, Relation.causality_right, Relation.unrelated, Relation.parallel, Relation.unrelated],
    "E": [Relation.causality_right, Relation.parallel, Relation.parallel, Relation.parallel, Relation.unrelated, Relation.causality_left],
    "F": [Relation.unrelated, Relation.causality_right, Relation.unrelated, Relation.unrelated, Relation.causality_right, Relation.unrelated],
}