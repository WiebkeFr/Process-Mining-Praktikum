import React, { useState } from 'react';
import Header from './components/structure/header';
import Intro from './components/structure/intro';
import Loading from './components/structure/loading';
import Layout from './components/style/layout';
import { GlobalStyles } from './components/style/global-styles';
import styled, { ThemeProvider } from 'styled-components';
import { lightTheme } from './components/style/theme';
import UploadButton from './components/actions/upload-button';
import Visualization from './components/visualization/net-vis';
import {
  Algorithm,
  DependencyNet,
  Parameter,
  Petrinet,
  State,
  initialPetrinet,
  initialDependencyNet,
} from './components/types';
import { I18nextProvider } from 'react-i18next';
import i18n from './i18n';
import Instruction from './components/structure/instruction';
import ParameterFields from './components/actions/parameter-fields';
import Footer from './components/structure/footer';
import References from './components/structure/references';
import Accordion from './components/structure/accordion';
import DownloadButton from './components/actions/download-button';

const ActionWrapper = styled.div`
  display: flex;
`;
const App = () => {
  const [algorithm, setAlgorithm] = useState<Algorithm>(Algorithm.Alpha);
  const [state, setState] = useState<State>(State.Start);

  const [parameter, setParameter] = useState<Parameter>({
    dep_threshold: 0.4,
    min_edge: 2,
  });

  const [petrinet, setPetrinet] = useState<Petrinet>(initialPetrinet);

  const [dependencynet, setDependencynet] =
    useState<DependencyNet>(initialDependencyNet);

  const handleAlgorithmChange = (state: Algorithm) => {
    setAlgorithm(state);
    setPetrinet(initialPetrinet);
    setDependencynet(initialDependencyNet);
  };

  return (
    <ThemeProvider theme={lightTheme}>
      <I18nextProvider i18n={i18n}>
        <GlobalStyles />
        <Header
          algorithm={algorithm}
          setAlgorithm={(state: Algorithm) => handleAlgorithmChange(state)}
        />
        <Layout>
          <Intro algorithm={algorithm} />
          {algorithm == Algorithm.Heuristic && (
            <ParameterFields
              parameter={parameter}
              setParameter={(state: Parameter) => setParameter(state)}
            />
          )}
          <Instruction />
          <ActionWrapper>
            <UploadButton
              setState={(state: State) => setState(state)}
              setPetrinet={(net) => setPetrinet(net)}
              setDependencynet={(net) => setDependencynet(net)}
              algorithm={algorithm}
              parameter={parameter}
            />
            <DownloadButton petrinet={petrinet} dependencynet={dependencynet} />
          </ActionWrapper>
          <Visualization
            petrinet={petrinet}
            dependencynet={dependencynet}
            algorithm={algorithm}
          />
          <Accordion
            petrinet={petrinet}
            dependencynet={dependencynet}
            algorithm={algorithm}
          />
          {state == State.Loading && (
            <Loading
              text={
                algorithm == Algorithm.Alpha
                  ? 'Running the Alpha Miner ...'
                  : 'Running the Heuristic Miner ...'
              }
            />
          )}
          <References />
        </Layout>
        <Footer
          algorithm={algorithm}
          setAlgorithm={(state: Algorithm) => handleAlgorithmChange(state)}
        />
      </I18nextProvider>
    </ThemeProvider>
  );
};

export default App;
