import React from 'react';
import styled from 'styled-components';

const StyledTable = styled.table`
  display: block;
  overflow-y: scroll;
  border-collapse: collapse;
`;

const StyledRow = styled.tr``;

const StyledCell = styled.td<{ isHighlighted?: boolean }>`
  padding: 8px 16px;
  border: 1px solid lightgray;
  font-weight: ${({ isHighlighted }) => (isHighlighted ? 'bold' : 'normal')};
  text-align: right;
`;

interface MatrixVisualizationProps {
  columns: Array<String>;
  matrix: Array<Array<String>>;
}

/**
 * This component displays a matrix.
 */
const MatrixVisualization: React.FC<MatrixVisualizationProps> = ({
  columns,
  matrix,
}) => {
  const columnLables = [...columns];
  matrix.unshift(columnLables);
  const rowLables = [...columns];
  rowLables.unshift('');
  matrix.forEach((row, index) => {
    row.unshift(rowLables[index]);
  });

  return (
    <StyledTable>
      <tbody>
        {matrix.map((row, rowIndex) => (
          <StyledRow key={rowIndex}>
            {row.map((column, columnIndex) => (
              <StyledCell
                key={columnIndex}
                isHighlighted={rowIndex == 0 || columnIndex == 0}
              >
                {column}
              </StyledCell>
            ))}
          </StyledRow>
        ))}
      </tbody>
    </StyledTable>
  );
};

export default MatrixVisualization;
