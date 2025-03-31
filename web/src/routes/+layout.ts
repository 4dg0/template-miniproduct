import { PUBLIC_POSTHOG_HOST, PUBLIC_POSTHOG_TOKEN } from '$env/static/public';
import posthog from 'posthog-js';
import { browser } from '$app/environment';

import { pbInitPromise } from '$lib/config/pb';
import { subscribeUser } from '$lib/providers/user.svelte';

export const prerender = true;

export const load = async () => {
	await pbInitPromise;

	subscribeUser();

	if (browser) {
		posthog.init(PUBLIC_POSTHOG_TOKEN, {
			api_host: PUBLIC_POSTHOG_HOST,
			person_profiles: 'always'
		});
		posthog.capture('Posthog initialized');
	}

	return;
};
