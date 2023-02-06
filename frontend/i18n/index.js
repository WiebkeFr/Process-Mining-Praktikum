import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

import en from './locales/en.json';
import de from './locales/de.json';

const resources = { en: { translation: en }, de: { translation: de } };

i18n.use(initReactI18next).init({
  resources,
  lng: 'en',
  languages: ['en', 'de'],
  supportedLngs: ['en', 'de'],
  interpolation: { escapeValue: false },
  transKeepBasicHtmlNodesFor: ['br', 'strong', 'i'],
});

export default i18n;
