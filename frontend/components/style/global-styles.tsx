import {
  createGlobalStyle,
  DefaultTheme,
  GlobalStyleComponent,
} from 'styled-components';

interface GlobalStyleProps {
  background?: string;
  body?: string;
  text?: string;
}

export const GlobalStyles: GlobalStyleComponent<
  { theme: GlobalStyleProps },
  DefaultTheme
> = createGlobalStyle`
    body {
        margin: 0;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
        'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
        sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        background: ${({ theme }) => theme.body};
        color: ${({ theme }) => theme.text};
        font-family: Helvetica, Arial, Roboto, sans-serif;
        transition: all 0.50s linear;
    }
    
    code {
        font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
        monospace;
    }
    
    :root {
        --background: white;
        --text-primary: #363537;
        --text-secondary: #360ccc;
        --accent: #064ccc;
        --button: #1c67ee;
    }
`;
