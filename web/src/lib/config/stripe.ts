import { PUBLIC_STRIPE_KEY } from '$env/static/public';
import { loadStripe, type Stripe } from '@stripe/stripe-js';

export let stripe: Stripe | null = null;

export const initStripe = async () => {
	stripe = await loadStripe(PUBLIC_STRIPE_KEY);
};
