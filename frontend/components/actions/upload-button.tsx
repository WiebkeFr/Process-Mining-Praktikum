import React from 'react';
import { useRef } from 'react';
import { useTranslation } from 'react-i18next';
import styled from 'styled-components';
import {
  getInQuotationMarks,
  getPlacesAsDOT,
  getFlowAsDOT,
  getEdgesAsDOT,
  convertToRelations,
} from '../visualization/dot-utils';
import {
  Algorithm,
  Petrinet,
  PetrinetResponse,
  Parameter,
  State,
  DependencyNetResponse,
  DependencyNet,
  initialDependencyNet,
  initialPetrinet,
} from '../types';

const StyledInput = styled.input`
  display: none;
`;

const StyledLabel = styled.label`
  display: block;
  width: fit-content;
  white-space: nowrap;
  border-radius: 20px;
  padding: 12px 24px;
  margin: 24px 0px;
  color: #ffffff;
  background-color: var(--button);
  font-weight: bold;
  cursor: pointer;
  transition: 0.5s all;

  &:hover {
    background-color: var(--accent);
  }
`;

interface UploadButtonProps {
  setState: (state: State) => void;
  setPetrinet: (state: Petrinet) => void;
  setDependencynet: (state: DependencyNet) => void;
  algorithm: Algorithm;
  parameter: Parameter;
}

/**
 * The purpose of this component is:
 *  - to show the upload-button
 *  - to fetch the petri-net/dependency-net from the backend
 *  - to convert the nets (places and flows) into strings which are concatinated to the graph
 */
const UploadButton: React.FC<UploadButtonProps> = ({
  setState,
  setPetrinet,
  setDependencynet,
  algorithm,
  parameter,
}) => {
  const fileInput = useRef<HTMLInputElement>(null);
  const { t } = useTranslation();

  /**
   * Extracts the file to be uploaded from the event
   *
   * @param event - FormEvent
   */
  const onFileChange = (event: React.FormEvent) => {
    event.preventDefault();
    if (fileInput && fileInput.current && fileInput.current.files) {
      uploadFile(fileInput.current.files[0]);
    }
  };

  /**
   * Fetches a net from the xes-file using the alpha-miner or the heuristic miner
   * and sets the result as the current Petrinet respectively Dependency-net
   *
   * @param file - The xes-file to be uploaded
   */
  const uploadFile = (file: File) => {
    setState(State.Loading);
    const formData = new FormData();
    formData.append('file', file);
    if (!window) {
      return;
    }

    const href = `${window.location.href}${
      algorithm == Algorithm.Alpha
        ? 'alpha-miner'
        : `heuristic-miner?dep_threshold=${parameter.dep_threshold}&min_edge=${parameter.min_edge}`
    }`;

    fetch(href, {
      method: 'POST',
      body: formData,
    })
      .then((response) => {
        return response.json();
      })
      .then((response: PetrinetResponse | DependencyNetResponse) => {
        setState(State.Success);
        if (algorithm == Algorithm.Alpha) {
          response = response as PetrinetResponse;
          const petrinet_T_L = response.T_L.map((t) => getInQuotationMarks(t));
          const petrinet_P_L = response.P_L.map((p) => getPlacesAsDOT(p));
          const petrinet_F_L = response.F_L.map((f) => getFlowAsDOT(f));
          const petrinet_footprint = response.footprint_matrix.map((row) =>
            convertToRelations(row)
          );
          setPetrinet({
            T_L: petrinet_T_L,
            P_L: petrinet_P_L,
            F_L: petrinet_F_L,
            footprint_matrix: petrinet_footprint,
          });
        } else {
          response = response as DependencyNetResponse;
          const depnet_T_L = response.T_L.map((t) => getInQuotationMarks(t));
          const depnet_F_L = response.F_L.map((f) => getEdgesAsDOT(f));
          setDependencynet({
            T_L: depnet_T_L,
            F_L: depnet_F_L,
            frequency_matrix: response.frequency_matrix,
            dependency_matrix: response.dependency_matrix,
            parameters: parameter,
          });
        }
      })
      .catch((error) => {
        console.log(error);
        setPetrinet(initialPetrinet);
        setDependencynet(initialDependencyNet);
        setState(State.Error);
      });
  };

  return (
    <div>
      <StyledLabel>
        {t<string>('action.upload')}
        <StyledInput
          type="file"
          accept=".xes"
          onChange={onFileChange}
          ref={fileInput}
          onClick={(event) => {
            (event.target as HTMLInputElement).value = '';
          }}
        />
      </StyledLabel>
    </div>
  );
};

export default UploadButton;
