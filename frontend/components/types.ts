export enum Algorithm {
  Alpha,
  Heuristic,
}

export enum State {
  Start,
  Loading,
  Error,
  Success,
}

export interface PetrinetResponse {
  T_L: Array<String>;
  P_L: Array<Array<String> | String>;
  F_L: Array<Array<Array<String>> | String>;
  footprint_matrix: Array<Array<String>>;
}

export interface DependencyNetResponse {
  T_L: Array<String>;
  F_L: Array<[string, string, number, number]>;
  frequency_matrix: Array<Array<String>>;
  dependency_matrix: Array<Array<String>>;
}

export interface Petrinet {
  T_L: Array<String>;
  P_L: Array<String>;
  F_L: Array<String>;
  footprint_matrix: Array<Array<String>>;
}

export interface DependencyNet {
  T_L: Array<String>;
  F_L: Array<String>;
  frequency_matrix: Array<Array<String>>;
  dependency_matrix: Array<Array<String>>;
  parameters: Parameter;
}

export interface Parameter {
  dep_threshold: number;
  min_edge: number;
}

export const initialPetrinet = {
  T_L: [],
  P_L: [],
  F_L: [],
  footprint_matrix: [],
} as Petrinet;

export const initialDependencyNet = {
  T_L: [],
  F_L: [],
  frequency_matrix: [],
  dependency_matrix: [],
  parameters: {
    dep_threshold: 0.4,
    min_edge: 2,
  },
} as DependencyNet;
