import { browser } from '$app/environment';
import { PUBLIC_PB_URL } from '$env/static/public';
import PocketBase, { AsyncAuthStore } from 'pocketbase';

function initUserProvider() {
	if (!browser) {
		return '';
	}
	return localStorage.getItem('pb_auth') ?? '';
}

const store = new AsyncAuthStore({
	save: async (serialized: string) => {
		localStorage.set({
			key: 'pb_auth',
			value: serialized
		});
	},
	initial: initUserProvider(),
	clear: async () => {
		localStorage.removeItem('pb_auth');
	}
});

export const pb = new PocketBase(PUBLIC_PB_URL, store);
