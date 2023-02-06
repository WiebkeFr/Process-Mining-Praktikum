# Dependency Graph Example on Page 202 [1]

event0_reduced = { # 5 occurences
    "case": ["a0", "a0"],
    "index": [0, 1],
    "event": [ "A", "E"],  
}

event1_reduced = { # 10 occurences
    "case": ["b0", "b0", "b0", "b0"],
    "index": [0, 1, 2, 3],
    "event": [ "A", "B", "C", "E"],  
}

event2_reduced = { # 10 occurences
    "case": ["c0", "c0", "c0", "c0"],
    "index": [0, 1, 2, 3],
    "event": [ "A", "C", "B", "E"],  
}

event3 = { # 1 occurences of each case
    "case": ["d0", "d0", "d0", "d1", "d1", "d1", "d2", "d2", "d2", "d2", "d2"],
    "index": [0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4],
    "event": ["A", "B", "E", "A", "C", "E", "A", "D", "D", "D", "E"],
}

event4_reduced = { # 10 occurences
    "case": ["e0", "e0", "e0"],
    "index": [0, 1, 2],
    "event": [ "A", "D", "E"],  
}

event5 = { # 1 occurence
    "case": ["f0", "f0", "f0", "f0", "f1", "f1", "f1", "f1"],
    "index": [0, 1, 2, 3, 0, 1, 2, 3],
    "event": [ "A", "D", "D", "E", "A", "D", "D", "E"],
}


frequency_matrix_solution = {
    "A": [0, 0, 0, 0, 0], 
    "B": [11, 0, 10, 0, 0],
    "C": [11, 10, 0, 0, 0],
    "D": [13, 0, 0, 4, 0],
    "E": [5, 11, 11, 13, 0]
}

dependency_matrix_solution = {
    "A": [0, -0.92, -0.92, -0.93, -0.83],
    "B": [0.92, 0, 0, 0, -0.92],
    "C": [0.92, 0, 0, 0, -0.92],
    "D": [0.93, 0, 0, 0.80, -0.93],
    "E": [0.83, 0.92, 0.92, 0.93, 0]
}

min_edge0 = 2
dep_thresh0 = 0.7
edges0_solution = [
    ("A", "E", "5", "0.83"), ("A", "D", "13", "0.93"), ("D", "E", "13", "0.93"),
    ("A", "B", "11", "0.92"), ("C", "E", "11", "0.92"), ("B", "E", "11", "0.92"),
    ("A", "C", "11", "0.92"), ("D", "D", "4", "0.8"), 
]

min_edge1 = 5
dep_thresh1 = 0.9
edges1_solution = [
    ("A", "D", "13", "0.93"), ("D", "E", "13", "0.93"),
    ("A", "B", "11", "0.92"), ("C", "E", "11", "0.92"), 
    ("B", "E", "11", "0.92"), ("A", "C", "11", "0.92")
]


data2 = {
        "case": ["c0", "c0", 
                 "c1", "c1", "c1",
                 "c2", "c2", "c2", "c2"],
        "index": [0, 1,  
                  0, 1, 2, 
                  0, 1, 2, 3],
        "event": ["A", "C",
                  "A", "B", "C",
                  "A", "B", "B", "C"]
}

frequency_matrix_solution2 = {
    "A": [0, 0, 0],
    "B": [2, 1, 0],
    "C": [1, 2, 0]
}

dependency_matrix_solution2 = {
    "A": [0, -0.67, -0.50],
    "B": [0.67, 0.50, -0.67],
    "C": [0.50, 0.67, 0]
}

min_edge2 = 1
dep_thresh2 = 0.5
edges2_solution = [('A', 'B', '2', '0.67'), ('B', 'B', '1', '0.5'), ('A', 'C', '1', '0.5'), 
('B', 'C', '2', '0.67')]

min_edge3 = 1
dep_thresh3 = 0.6
edges3_solution = [('A', 'B', '2', '0.67'), ('B', 'C', '2', '0.67')]