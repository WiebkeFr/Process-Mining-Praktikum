import { Petrinet, Algorithm, DependencyNet } from '../types';

/**
 * Converts petrinet or dependency-net (dependent on selected algorithm) to a DOT graph
 *
 * @param {Petrinet | DependencyNet} net - places
 * @param {Algorithm} algorithm - places
 * @return {string} - DOT Graph
 */
export const computeGraph = (
  net: Petrinet | DependencyNet,
  algorithm: Algorithm
) => {
  if (algorithm == Algorithm.Alpha) {
    const petrinet = net as Petrinet;
    return `
        digraph {
            graph [center=true margin=1 rankdir=LR]{
                subgraph places {
                  node [ shape=circle, label="" ]
                    ${petrinet.P_L.filter((node) => node != 'iL').join(' ')}
                    iL [ label=<<font point-size="8">&#9899;</font>> ]
                }
                subgraph transitions {
                  node [ shape=square, height=.7 ]
                    ${petrinet.T_L.join(' ')}
                }
            }
            ${petrinet.F_L.join(' ')}
            overlap=false
        }
        `;
  }

  return `
        digraph {
        graph [center=true margin=1 rankdir=LR]{
            subgraph transitions {
                node [ shape=square, style=rounded ]
                ${net.T_L.filter((node) => node != 'iL' && node != 'oL').join(
                  ' '
                )}
                node [ shape=circle, label="" ]
                iL oL
            }
        }
        ${net.F_L.join(' ')}
        overlap=false
        }
    `;
};
