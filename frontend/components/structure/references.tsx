import React from 'react';
import { useTranslation } from 'react-i18next';
import styled from 'styled-components';

const StyledReferenceWrapper = styled.div`
  margin-top: 60px;
`;

const StyledSubHeadline = styled.div`
  padding: 12px 0px 8px;
  font-size: 24px;
  font-weight: bold;
`;

const StyledLink = styled.div`
  padding: 8px 0px;
  font-size: 18px;
  line-height: 24px;
`;

/**
 * This component shows the reference list.
 */
const References: React.FC = () => {
  const { t } = useTranslation();

  return (
    <StyledReferenceWrapper>
      <StyledSubHeadline>{t<string>('reference')}</StyledSubHeadline>
      <StyledLink>
        Van der Aalst, Wil M. P.. <i>Process Mining: Data Science in Action</i>,
        Springer Berlin / Heidelberg, 2016. ProQuest Ebook Central,{' '}
        <a>
          https://ebookcentral.proquest.com/lib/munchentech/detail.action?docID=4505537.
        </a>
      </StyledLink>
      <StyledLink>
        Weijters, A.J., van der Aalst, W.M., &amp; Medeiros, A.K. (2006):{' '}
        <i>Process mining with the HeuristicsMiner algorithm.</i>
      </StyledLink>
    </StyledReferenceWrapper>
  );
};

export default References;
