import React from 'react';
import styled from 'styled-components';
import SyncLoader from 'react-spinners/SyncLoader';

const StyledBackground = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(5px);
  transition: 1s all;
`;

const StyledModal = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  position: absolute;
  top: 30%;
  left: 0;
  right: 0;
  margin-left: auto;
  margin-right: auto;
  padding: 16px;
  width: fit-content;
  border-radius: 6px;
`;

const StyledLoaderText = styled.p`
  padding: 16px 0px;
  color: black;
  font-size: 20px;
`;

interface LoadingProps {
  text: string;
}

/**
 * This component defines the loading overlay.
 */
const Loading = ({ text }: LoadingProps) => {
  return (
    <StyledBackground>
      <StyledModal>
        <SyncLoader />
        <StyledLoaderText>{text}</StyledLoaderText>
      </StyledModal>
    </StyledBackground>
  );
};

export default Loading;
