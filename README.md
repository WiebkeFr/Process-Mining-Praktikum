# Process Mining Praktikum

## What is this project?

This is a tool to process and visualize event logs using the Alpha Miner Algorithm or the Heuristic Miner. The project is separated in the frontend and the webservice. In the first part, a XES-file is uploaded and the petrinet or respectively the dependency-net is visualized. The webservice executes the selected algorithm and returns the result.

## How to run the project?

### 1. Clone repository

```bash
git clone https://gitlab.lrz.de/wiebkefreitag/process-mining-praktikum.git
```

### 2. Start virtual environment

```bash
python3 -m venv venv && source venv/bin/activate
```

### 3. Installation

```bash
npm install --force                    # installs frontend dependencies
pip3 install -r requirements.txt       # installs backend dependencies
```

### 4. Start webservice and frontend

```bash
npm run build
export FLASK_APP=webserver.py
flask run --host="::1" --port=9009
```

## How to run the tests?

After the installation and start of the virtual environment, you can also start the test. In order to do that, you need to run the command below:

```bash
pytest -v
```

## What are the endpoints of the webservice?

### Alpha Miner Algorithm

Description of the endpoint:

```plaintext
POST /alpha-miner
```

Attributes:

| Attribute                | Type     | Required               | Description           |
|:----------------------- | :------- | :--------------------- | :-------------------- |
| `file` | File | Yes | The files of the request must include one file of the type **xes** which contains the event logs to be processes. More information about the file-type can be found here https://fluxicon.com/blog/2010/09/intro-to-xes/ |

Response body attributes:

| Attribute | Type     | Description           |
| :-------- | :------- | :-------------------- |
| `T_L`     | Array\<String> | T_L are the names of all events (event-nodes of petrinets). |
| `P_L`     | Array\<Array\<String> \| String> | P_L are the places of transitions (transition-nodes of petrinets). |
| `F_L`     | Array\<Array\<Array\<String>> \| String> | F_L are the flows (edges) of the petrinet. |
| `footprint_matrix`     | Array\<Array\<String>> | The footprint-matrix showing the relation between each event-pair. |

Example response:

```json
{
  "T_L": ["a", "b", "c"],
  "P_L": [[["a"], ["b", "c"]], "iL", "oL"],
  "F_L": [["a", [["a"], ["b", "c"]]], ["iL", "a"], ["c", "oL"], ["b", "oL"]],
  "footprint_matrix": [["unrelated", "causality_right","causality_right"], 
    ["unrelated", "unrelated", "parallel"], 
    ["unrelated", "parallel", "unrelated"]]
}
```

### Heuristic Miner Algorithm

Description of the endpoint:

```plaintext
POST /heuristic-miner
```

Attributes:

| Attribute                | Type     | Required               | Description           |
| :----------------------- | :------- | :--------------------- | :-------------------- |
| `file`  | File | Yes | The files of the request must include one file of the type **xes** which contains the event logs to be processes. More information about the file-type can be found here https://fluxicon.com/blog/2010/09/intro-to-xes/ |
| `dep_threshold`  | number | Yes | Parameter of the Heuristic Miner: Dependency threshold (default: 0.4)|
| `min_edge`  | number | Yes | Parameter of the Heuristic Miner: Minimum occurences of edges (default: 5)|


Response body attributes:

| Attribute | Type     | Description           |
| :-------- | :------- | :-------------------- |
| `T_L`     | Array<String> | T_L are the names of all events |
| `F_L`     | Array<[string, string, string, string]> | F_L are the flows (edges) of the dependency-nets including the frequency and dependency. |
| `frequency_matrix`     | Array\<Array\<String>> | The frequency-matrix displays the frequency between each pair of events. |
| `dependency_matrix`     | Array\<Array\<String>> | The dependency-matrix shows the dependency between each pair of events. |

Example response:

```json
{
  "T_L": ["a", "b", "c"],
  "F_L": [["iL", "a", "7", "0.88"], ["a", "b", "3", "0.75"], ["a", "c", "4", "0.75"],
    ["b", "b", "4", "0.88"], ["b", "oL", "3", "0.75"], ["c", "oL", "4", "0.75"]
  ],
  "frequency_matrix": [["0", "3", "4"], ["0", "4", "0"] ,["0", "0", "0"]],
  "dependency_matrix": [["0", "0.75", "0.75"], ["-0.75", "0.88", "0"] ,["-0.75", "0", "0"]],
}
```

## How is the the frontend structured?

The main-page of the frontend is located in the `App.tsx` which is the place of the current state and page context (selected algorithm, nets and parameter).

The components are separated into the three following parts:

```shell
components
  |-> actions
  |-> structure         
  |-> style
  |-> visualization
```

The first subfolder contains items which require `action` by the user like buttons (upload), the parameter-fields and the language-selection.

The folder `structure` includes all components which provide structure to the page such as the navigation (header and footer) and the text-elements like the introduction, instructions on how to use the tool and references. Other components e.g. the accordion and loading- and error-message are located there as well.

The `style`-folder includes the layout, theme and global-styles.

The components to visualize the petrinet, dependency-net and matrices are in the `visualization`-folder which also includes helper-functions to the conversion into DOT language.

