import React from 'react';
import { useTranslation } from 'react-i18next';
import styled from 'styled-components';
import { Algorithm } from '../types';
import LanguageSwitch from '../actions/language-switch';

const FooterWrapper = styled.footer`
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  margin-top: -10px;
  padding: 40px;
  background: linear-gradient(184deg, #064ccc 55%, #360ccc);
  clip-path: polygon(0 40%, 100% 0%, 100% 100%, 0% 100%);
`;

const StyledButton = styled.button<{ highlighted: boolean }>`
  height: 35px;
  font-weight: bold;
  font-size: 18px;
  transition: 0.3s all;
  border: none;
  cursor: pointer;
  background: unset;
  color: ${({ highlighted }) => (highlighted ? 'white' : 'black')};

  &:hover {
    color: white;
  }
`;

interface FooterProps {
  algorithm: Algorithm;
  setAlgorithm: (state: Algorithm) => void;
}

/**
 * This component defines the footer of the website, which includes:
 *  - the buttons to select the algorithm
 *  - language selection
 */
const Footer: React.FC<FooterProps> = ({ algorithm, setAlgorithm }) => {
  return (
    <FooterWrapper>
      <LanguageSwitch isLight={false} />
      <StyledButton
        highlighted={Algorithm.Alpha == algorithm}
        onClick={() => setAlgorithm(Algorithm.Alpha)}
      >
        Alpha Miner
      </StyledButton>
      <StyledButton
        highlighted={Algorithm.Heuristic == algorithm}
        onClick={() => setAlgorithm(Algorithm.Heuristic)}
      >
        Heuristic Miner
      </StyledButton>
    </FooterWrapper>
  );
};

export default Footer;
