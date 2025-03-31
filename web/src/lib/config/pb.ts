import { browser } from '$app/environment';
import { PUBLIC_PB_URL } from '$env/static/public';
import { UserSchema } from '$lib/models/user';
import { userProvider } from '$lib/providers/user.svelte';
import { Preferences } from '@capacitor/preferences';
import PocketBase, { AsyncAuthStore } from 'pocketbase';

async function initUserProvider() {
	if (!browser) {
		return '';
	}

	const res = await Preferences.get({ key: 'pb_auth' });
	if (res.value) userProvider.set(UserSchema.parse(JSON.parse(res.value).record));
	return res.value ?? '';
}

export const pbInitPromise = initUserProvider();

const store = new AsyncAuthStore({
	save: async (serialized: string) => {
		await Preferences.set({
			key: 'pb_auth',
			value: serialized
		});
	},
	initial: pbInitPromise,
	clear: async () => {
		await Preferences.remove({ key: 'pb_auth' });
	}
});

export const pb = new PocketBase(PUBLIC_PB_URL, store);
