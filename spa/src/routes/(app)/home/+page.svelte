<script lang="ts">
	import { createCheckoutSession } from '$lib/features/payment';
	import { userProvider } from '$lib/providers/user.svelte';

	const user = $derived(userProvider.user);

	const onPay = async () => {
		await createCheckoutSession();
	};
</script>

<div class="flex flex-col gap-4">
	<button onclick={onPay} class="rounded border p-4"> Pay with Stripe </button>

	<div>
		{JSON.stringify(user)}
	</div>
</div>
