import React from 'react';
import { Trans, useTranslation } from 'react-i18next';
import styled from 'styled-components';
import { Algorithm } from '../types';

const StyledIntroWrapper = styled.div``;

const StyledIntroHeadline = styled.div`
  margin-top: 150px;
  margin-bottom: 30px;
  padding: 16px 0px;
  font-size: 52px;
  font-weight: bold;
  line-height: 35px;
`;

const StyledIntroSubHeadline = styled.div`
  padding: 12px 0px 12px;
  font-size: 24px;
  font-weight: bold;
  line-height: 40px;
`;

const StyledIntroText = styled.div`
  padding: 8px 0px;
  font-size: 18px;
  line-height: 30px;
  white-space: pre-line;
`;

interface IntroProps {
  algorithm: Algorithm;
}

/**
 * This component defines the introduction/explanation of the algorithm to be run.
 */
const Intro: React.FC<IntroProps> = ({ algorithm }) => {
  const { t, i18n } = useTranslation();

  return (
    <StyledIntroWrapper>
      <StyledIntroHeadline>{t<string>('title')}</StyledIntroHeadline>
      <StyledIntroSubHeadline>{t<string>('intro')}</StyledIntroSubHeadline>
      {algorithm == Algorithm.Alpha ? (
        <StyledIntroText>
          <Trans i18nKey="alpha.explanation" components={[<strong />]} />
        </StyledIntroText>
      ) : (
        <StyledIntroText>
          <Trans i18nKey="heuristic.explanation" components={[<strong />]} />
        </StyledIntroText>
      )}
    </StyledIntroWrapper>
  );
};

export default Intro;
