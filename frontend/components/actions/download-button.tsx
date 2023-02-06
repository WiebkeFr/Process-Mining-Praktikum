import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import styled from 'styled-components';
import * as svg from 'save-svg-as-png';
import { useEffect } from 'react';
import { Petrinet, DependencyNet } from '../types';

const StyledButton = styled.button`
  display: block;
  width: fit-content;
  margin: 24px;
  padding: 12px 24px;
  border-radius: 20px;
  border: unset;
  cursor: pointer;
  color: #ffffff;
  background-color: var(--button);
  white-space: nowrap;
  font-size: 16px;
  font-weight: bold;
  transition: 0.5s all;

  &:hover {
    background-color: var(--accent);
  }
`;

interface DownloadButtonProps {
  petrinet: Petrinet;
  dependencynet: DependencyNet;
}

/**
 * This component shows the download-button
 */
const DownloadButton: React.FC<DownloadButtonProps> = ({
  petrinet,
  dependencynet,
}) => {
  // no net yet
  if (petrinet.T_L.length == 0 && dependencynet.T_L.length == 0) {
    return <div />;
  }

  const { t } = useTranslation();

  const handleDownload = () => {
    const graph = document.getElementsByClassName('graph-visualization');
    if (graph.length == 0) return;
    const svgElement = graph[0].firstElementChild;
    svg.svgAsPngUri(svgElement, {}).then((uri: any) => {
      const link = document.createElement('a');
      link.href = uri;
      link.setAttribute('download', 'graph.png');
      document.body.appendChild(link);
      link.click();
      link.remove();
    });
  };

  return (
    <StyledButton onClick={handleDownload}>
      {t<string>('action.download')}
    </StyledButton>
  );
};

export default DownloadButton;
