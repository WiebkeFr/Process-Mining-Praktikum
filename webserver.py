from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from flask import request
from flask import jsonify
import numpy as np

from webservice.src.read_xes import get_dataframe_from_xes_file
from webservice.src.alpha_algorithm import run_alpha_algorithm
from webservice.src.heuristic_algorithm import run_heuristic_algorithm

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/")
def develop_frontend():
    return render_template("index.html")


@app.route("/alpha-miner", methods=["POST"])
@cross_origin(supports_credentials=True)
def alpha():
    file = request.files["file"]
    print(file, "was received")
    event_df = get_dataframe_from_xes_file(file)
    T_L, P_L, F_L, footprint_matrix = run_alpha_algorithm(event_df)
    return (
        jsonify(
            {
                "T_L": np.array(T_L, dtype=object).tolist(),
                "P_L": np.array(P_L, dtype=object).tolist(),
                "F_L": np.array(F_L, dtype=object).tolist(),
                "footprint_matrix": np.array(footprint_matrix, dtype=object).tolist()
            }
        ),
        200,
    )


@app.route("/heuristic-miner", methods=["POST"])
@cross_origin(supports_credentials=True)
def heuristic():
    file = request.files["file"]
    dep_threshold = request.args.get('dep_threshold')
    min_edge = request.args.get('min_edge')
    print(file, "was received")
    event_df = get_dataframe_from_xes_file(file)
    T_L, F_L, frequency_matrix, dependency_matrix = run_heuristic_algorithm(event_df, dep_threshold, min_edge)
    return (
        jsonify(
            {
                "T_L": np.array(T_L, dtype=object).tolist(),
                "F_L": np.array(F_L, dtype=object).tolist(),
                "frequency_matrix": np.array(frequency_matrix, dtype=object).tolist(),
                "dependency_matrix": np.array(dependency_matrix, dtype=object).tolist(),
            }
        ),
        200,
    )
