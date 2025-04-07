<script lang="ts">
	import '../app.css';
	import { onMount } from 'svelte';
	import { subscribeUser } from '$lib/providers/user.svelte';
	import { initPosthog } from '$lib/config/posthog';
	import { initStripe } from '$lib/config/stripe';

	import { settingsProvider } from '$lib/providers/settings.svelte';

	let { children } = $props();
	const lang = $derived(settingsProvider.lang);

	let userLoaded = $state(false);

	onMount(async () => {
		initPosthog();
		initStripe();

		await subscribeUser();
		userLoaded = true;
	});
</script>

{#if !userLoaded}
	<div class="flex h-screen w-screen items-center justify-center">
		<div
			class="border-secondary relative size-40 animate-spin rounded-full border-4 border-dashed"
		></div>
	</div>
{:else}
	{#key lang}
		{@render children()}
	{/key}
{/if}
