import React, { useState } from 'react';
import { useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import styled from 'styled-components';
import { Petrinet, DependencyNet, State, Algorithm } from '../types';
import MatrixVisualization from '../visualization/matrix-vis';

const StyledSubHeadline = styled.div`
  padding: 12px 0px 8px;
  font-size: 24px;
  font-weight: bold;
  margin: 50px 0px 20px;
`;

const AccordionWrapper = styled.div`
  box-shadow: 0 9px 31px rgb(0 0 0 / 7%), 0 2.71324px 9.34559px rgb(0 0 0 / 5%),
    0 1.12694px 3.88168px rgb(0 0 0 / 4%),
    0 0.407592px 1.40393px rgb(0 0 0 / 2%);
  border-radius: 8px;
  margin: 20px 0px 40px;
`;

const AccordionSlideTitel = styled.div<{ isOpen?: boolean }>`
  display: flex;
  justify-content: space-between;
  padding: 24px;
  border-bottom: ${({ isOpen }) => (isOpen ? '1px lightGray solid' : 'unset')};
  border-top: 1px lightGray solid;
  cursor: pointer;
  font-weight: bold;

  div {
    transform: rotate(${({ isOpen }) => (isOpen ? '-180deg' : '0')});
    svg > path {
      :hover {
        stroke: black;
      }
    }
    display: flex;
    align-items: center;
    transition: 0.5s transform ease-in-out;
  }

  &.first {
    border-top: unset;
  }

  &.last {
    border-bottom: ${({ isOpen }) =>
      isOpen ? '1px lightGray solid' : 'unset'};
  }

  &:hover {
    background-color: #e8e8e8;
  }
`;

const AccordionSlide = styled.div<{ isOpen?: boolean }>`
  max-height: ${({ isOpen }) => (isOpen ? '100%' : '0px')};
  padding: ${({ isOpen }) => (isOpen ? '24px 48px' : '0px 48px')};
  transition: 0.4s all ease-in-out;
  overflow: hidden;
`;

interface AccordionProps {
  petrinet: Petrinet;
  dependencynet: DependencyNet;
  algorithm: Algorithm;
}

/**
 * This component show the matrics/steps of the selected algorithm as an accordion.
 */
const Accordion: React.FC<AccordionProps> = ({
  petrinet,
  dependencynet,
  algorithm,
}) => {
  // no net yet
  if (petrinet.T_L.length == 0 && dependencynet.T_L.length == 0) {
    return <div />;
  }

  const { t } = useTranslation();
  const [cards, setCards] = useState<{ title: string; content: JSX.Element }[]>(
    []
  );
  const [state, setState] = useState([]);

  const generateAlphaAccordion = () => {
    const alphaCards = [
      {
        title: t('accordion.footprint'),
        content: (
          <MatrixVisualization
            columns={petrinet.T_L}
            matrix={petrinet.footprint_matrix}
          />
        ),
      },
    ];

    setCards(alphaCards);
    setState([true]);
  };

  const generateHeuristicAccordion = () => {
    const heuristicCards = [
      {
        title: t('accordion.parameter'),
        content: (
          <div>
            {t<string>('heuristic.parameter.dep_threshold')}:{' '}
            {dependencynet.parameters.dep_threshold}
            <br />
            {t<string>('heuristic.parameter.min_edge')}:{' '}
            {dependencynet.parameters.min_edge}
          </div>
        ),
      },
      {
        title: t('accordion.frequency'),
        content: (
          <MatrixVisualization
            columns={dependencynet.T_L}
            matrix={dependencynet.frequency_matrix}
          />
        ),
      },
      {
        title: t('accordion.dependency'),
        content: (
          <MatrixVisualization
            columns={dependencynet.T_L}
            matrix={dependencynet.dependency_matrix}
          />
        ),
      },
    ];

    setCards(heuristicCards);
    setState([true, false]);
  };

  const handleClick = (index: number) => {
    const newState = [...state];
    newState[index] = !newState[index];
    setState(newState);
  };
  useEffect(() => {
    if (algorithm == Algorithm.Alpha) {
      generateAlphaAccordion();
    } else {
      generateHeuristicAccordion();
    }
  }, [petrinet, dependencynet]);

  return (
    <div>
      <StyledSubHeadline>{t<string>('accordion.title')}</StyledSubHeadline>
      <AccordionWrapper>
        {cards.map((card, index) => (
          <div key={index}>
            <AccordionSlideTitel
              className={`${index == 0 && 'first'} ${
                index == cards.length - 1 && 'last'
              }`}
              isOpen={state[index]}
              onClick={() => handleClick(index)}
            >
              {card.title}
              <div>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="12"
                  height="7"
                  viewBox="0 0 12 7"
                  fill="none"
                >
                  <path d="M1 1L6 5.5L11 1" stroke="gray" strokeWidth="2" />
                </svg>
              </div>
            </AccordionSlideTitel>
            <AccordionSlide isOpen={state[index]}>
              {card.content}
            </AccordionSlide>
          </div>
        ))}
      </AccordionWrapper>
    </div>
  );
};

export default Accordion;
