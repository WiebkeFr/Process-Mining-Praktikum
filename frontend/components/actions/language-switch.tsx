import React from 'react';
import { useTranslation } from 'react-i18next';
import styled from 'styled-components';

const StyledSelect = styled.select<LanguageSwitchProps>`
  background: unset;
  border: unset;
  height: 35px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  color: ${({ isLight }) => (isLight ? 'var(--text-primary)' : '#000000')};

  &:hover {
    color: ${({ isLight }) => (isLight ? 'var(--text-secondary)' : '#ffffff')};
    text-underline-offset: 6px;
  }
`;

interface LanguageSwitchProps {
  isLight: boolean;
}

/**
 * This component show a language switch (german and englisch)
 */
const LanguageSwitch: React.FC<LanguageSwitchProps> = ({ isLight }) => {
  const { i18n } = useTranslation();

  const setLanguage = (event: React.ChangeEvent<HTMLSelectElement>) => {
    i18n.changeLanguage(event.target.value);
  };

  return (
    <StyledSelect onChange={setLanguage} isLight={isLight}>
      <option value="en">EN</option>
      <option value="de">DE</option>
    </StyledSelect>
  );
};

export default LanguageSwitch;
