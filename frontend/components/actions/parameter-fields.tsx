import React from 'react';
import styled from 'styled-components';
import { Parameter } from '../types';
import { useTranslation } from 'react-i18next';

const StyledWrapper = styled.div`
  margin-top: 16px;
  margin-bottom: 32px;
  padding: 8px 0px 8px 24px;
  border-radius: 8px;
  box-shadow: 0 9px 31px rgb(0 0 0 / 7%), 0 2.71324px 9.34559px rgb(0 0 0 / 5%),
    0 1.12694px 3.88168px rgb(0 0 0 / 4%),
    0 0.407592px 1.40393px rgb(0 0 0 / 2%);
`;

const StyledTable = styled.table`
  width: 100%;
  border-collapse: collapse;
`;

const StyledCurrentState = styled.div`
  background-color: #e8e8e8;
  border-radius: 4px;
  padding: 4px;
  width: 35px;
  height: fit-content;
  margin: auto 0px;
  align-items: center;
`;

const StyledRange = styled.td`
  display: flex;
  flex-direction: column;
  margin: 0px 40px;
  margin-top: 10px;
`;

const StyledInterval = styled.div`
  display: flex;
  justify-content: space-between;
  padding: 0px 2px;
  margin-top: -1px;
`;

interface ParameterFieldsProps {
  parameter: Parameter;
  setParameter: (state: Parameter) => void;
}

// Constants which define the intervals of the parameters
const MIN_EDGE_RANGE = 0;
const MAX_EDGE_RANGE = 20;
const MIN_DEP_THRESHOLD = 0;
const MAX_DEP_THRESHOLD = 1;

/**
 * This component shows the parameter fields for the Heuristic Miner:
 *  - dependency threshold
 *  - minimum occurance of edges
 */
const ParameterFields: React.FC<ParameterFieldsProps> = ({
  parameter,
  setParameter,
}) => {
  const { t } = useTranslation();

  const setRange = (
    event: React.ChangeEvent<HTMLInputElement>,
    type: 'dep_threshold' | 'min_edge'
  ) => {
    const result = event.currentTarget.value.replace(/\D/g, '');

    if (type === 'dep_threshold') {
      setParameter({
        dep_threshold: (parseInt(result) * MAX_DEP_THRESHOLD) / 100,
        min_edge: parameter.min_edge,
      });
    } else {
      setParameter({
        min_edge: (parseInt(result) * MAX_EDGE_RANGE) / 100,
        dep_threshold: parameter.dep_threshold,
      });
    }
  };

  return (
    <StyledWrapper>
      <StyledTable>
        <tbody>
          <tr>
            <td>{t<string>('heuristic.parameter.dep_threshold')}</td>
            <StyledRange>
              <input
                type="range"
                defaultValue={
                  (parameter.dep_threshold * 100) / MAX_DEP_THRESHOLD
                }
                onChange={(event) => setRange(event, 'dep_threshold')}
                step="1"
                style={{ cursor: 'pointer' }}
              />
              <StyledInterval>
                <span>{MIN_DEP_THRESHOLD}</span>
                <span>{MAX_DEP_THRESHOLD}</span>
              </StyledInterval>
            </StyledRange>
            <td>
              <StyledCurrentState>{parameter.dep_threshold}</StyledCurrentState>
            </td>
          </tr>
          <tr>
            <td>{t<string>('heuristic.parameter.min_edge')}</td>
            <StyledRange>
              <input
                type="range"
                defaultValue={(parameter.min_edge * 100) / MAX_EDGE_RANGE}
                onChange={(event) => setRange(event, 'min_edge')}
                step={100 / MAX_EDGE_RANGE}
                style={{ cursor: 'pointer' }}
              />
              <StyledInterval>
                <span>{MIN_EDGE_RANGE}</span>
                <span>{MAX_EDGE_RANGE}</span>
              </StyledInterval>
            </StyledRange>
            <td>
              <StyledCurrentState>{parameter.min_edge}</StyledCurrentState>
            </td>
          </tr>
        </tbody>
      </StyledTable>
    </StyledWrapper>
  );
};

export default ParameterFields;
