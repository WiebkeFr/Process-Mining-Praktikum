import React from 'react';
import styled from 'styled-components';
import { Algorithm } from '../types';
import { useTranslation } from 'react-i18next';
import LanguageSwitch from '../actions/language-switch';

const StyledHeader = styled.header`
  position: fixed;
  top: 0;
  left 0;
  right: 0;
  height: 26px;
  padding: 20px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 18px;
  z-index: 4;
  background-color: ${({ theme }) => theme.header}; 

`;

const StyledNavigation = styled.div`
  display: flex;
  align-items: center;
`;

const StyledTitel = styled.div`
  font-weight: bold;
`;

const StyledButton = styled.button<{ highlighted: boolean }>`
  border: none;
  background: unset;
  font-weight: bold;
  font-size: 18px;
  transition: 0.3s color;
  cursor: pointer;
  color: ${({ highlighted }) =>
    highlighted ? 'var(--accent)' : 'var(--text-primary)'};

  &:hover {
    color: var(--accent);
  }
`;

const Separator = styled.div`
  margin: 0px 20px;
  width: 2px;
  height: 30px;
  transform: skewX(-10deg);
  background-color: gray;
`;

interface HeaderProps {
  algorithm: Algorithm;
  setAlgorithm: (state: Algorithm) => void;
}

/**
 * This component defines the header of the website, which includes:
 *  - the buttons to select the algorithm
 *  - language selection
 */
const Header: React.FC<HeaderProps> = ({ algorithm, setAlgorithm }) => {
  return (
    <StyledHeader>
      <StyledTitel>Process Mining</StyledTitel>
      <StyledNavigation>
        <StyledButton
          highlighted={Algorithm.Alpha == algorithm}
          onClick={() => setAlgorithm(Algorithm.Alpha)}
        >
          Alpha Miner
        </StyledButton>
        <Separator />
        <StyledButton
          highlighted={Algorithm.Heuristic == algorithm}
          onClick={() => setAlgorithm(Algorithm.Heuristic)}
        >
          Heuristic Miner
        </StyledButton>
        <Separator />
        <LanguageSwitch isLight={true} />
      </StyledNavigation>
    </StyledHeader>
  );
};

export default Header;
