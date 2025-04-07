import { PUBLIC_API_URL } from '$env/static/public';
import { stripe } from '$lib/config/stripe';

export const createCheckoutSession = async () => {
	const response = await fetch(`${PUBLIC_API_URL}/payment/stripe/create-checkout-session`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			customerId: 'cus_S50uAEZo99mLZN',
			lookupKey: '[template]_plus_monthly'
		})
	});
	if (!response.ok) {
		const error = await response.json();
		console.error('Error creating checkout session:', error);
		return;
	}

	const payload = await response.json();
	await stripe!.redirectToCheckout({ sessionId: payload.sessionId });
};
