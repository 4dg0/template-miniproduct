import { PUBLIC_POSTHOG_HOST, PUBLIC_POSTHOG_TOKEN } from '$env/static/public';
import posthog from 'posthog-js';

export const initPosthog = () => {
	posthog.init(PUBLIC_POSTHOG_TOKEN, {
		api_host: PUBLIC_POSTHOG_HOST,
		person_profiles: 'always'
	});
	posthog.capture('Posthog initialized');
};
