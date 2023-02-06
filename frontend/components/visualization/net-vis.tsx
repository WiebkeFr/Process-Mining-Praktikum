import React from 'react';
import styled from 'styled-components';
import { Graphviz } from 'graphviz-react';
import { Petrinet, Algorithm, DependencyNet } from '../types';
import { computeGraph } from './compute-graph';

const StyledPanel = styled.div`
  position: relative;
  margin: 20px 0px;
  border-radius: 8px;
  padding: 24px;
  transition: 0.5s;
  box-shadow: 0 9px 31px rgb(0 0 0 / 7%), 0 2.71324px 9.34559px rgb(0 0 0 / 5%),
    0 1.12694px 3.88168px rgb(0 0 0 / 4%),
    0 0.407592px 1.40393px rgb(0 0 0 / 2%);
`;

interface VisualizationProps {
  petrinet: Petrinet;
  dependencynet: DependencyNet;
  algorithm: Algorithm;
}

/**
 * This component visualizes the petrinet or dependency-net.
 */
const Visualization: React.FC<VisualizationProps> = ({
  petrinet,
  dependencynet,
  algorithm,
}) => {
  // there is not net yet
  if (petrinet.T_L.length == 0 && dependencynet.T_L.length == 0) {
    return <div />;
  }

  const graph =
    algorithm == Algorithm.Alpha
      ? computeGraph(petrinet, algorithm)
      : computeGraph(dependencynet, algorithm);

  return (
    <StyledPanel>
      <Graphviz
        className="graph-visualization"
        dot={graph}
        options={{ width: '100%', height: '50%', zoom: false, fit: true }}
      />
    </StyledPanel>
  );
};

export default Visualization;
