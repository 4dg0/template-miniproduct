import { browser } from '$app/environment';

import { subscribeUser } from '$lib/providers/user.svelte';
import { initStripe } from '$lib/config/stripe';
import { initPosthog } from '$lib/config/posthog';

export const prerender = true;

export const load = async () => {
	if (browser) {
		subscribeUser();

		initPosthog();
		initStripe();
	}

	return;
};
