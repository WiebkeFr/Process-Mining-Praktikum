import React from 'react';
import styled from 'styled-components';

const StyledContent = styled.main`
  max-width: 1000px;
  margin: 60px auto;
  padding: 0px 30px;
`;

/**
 * This component defines the layout of the main-content of the website.
 */
const Layout = ({ children }: any) => {
  return <StyledContent>{children}</StyledContent>;
};

export default Layout;
