import { browser } from '$app/environment';
import { getLocale } from '$lib/paraglide/runtime';

class SettingsProvider {
	lang: 'en' | 'ru' = $state('en');
	theme: 'light' | 'dark' = $state('dark');

	setLang(lang: 'en' | 'ru') {
		this.lang = lang;
	}

	setTheme(theme: 'light' | 'dark') {
		this.theme = theme;
	}
}

export const settingsProvider = new SettingsProvider();

if (browser) {
	const theme = localStorage.getItem('theme') as 'light' | 'dark';
	settingsProvider.setTheme(theme);

	const lang = getLocale();
	settingsProvider.setLang(lang as 'en' | 'ru');
}
