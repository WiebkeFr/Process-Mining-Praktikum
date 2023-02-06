import React from 'react';
import { useTranslation } from 'react-i18next';
import styled from 'styled-components';

const StyledIntroWrapper = styled.div``;

const StyledIntroSubHeadline = styled.div`
  padding: 12px 0px 8px;
  font-size: 24px;
  font-weight: bold;
`;

const StyledIntroText = styled.div`
  padding: 8px 0px;
  font-size: 18px;
  line-height: 30px;
  white-space: pre-line;
`;

/**
 * This component defines the instruction of the website:
 *  - how and what document to upload
 *  - how to download pdf
 */
const Instruction: React.FC = () => {
  const { t } = useTranslation();

  return (
    <StyledIntroWrapper>
      <StyledIntroSubHeadline>
        {t<string>('instruction.title')}
      </StyledIntroSubHeadline>
      <StyledIntroText>{t<string>('instruction.explanation')}</StyledIntroText>
    </StyledIntroWrapper>
  );
};

export default Instruction;
