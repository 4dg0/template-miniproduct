<script lang="ts">
	import { goto } from '$app/navigation';
	import { userProvider } from '$lib/providers/user.svelte';
	import { onMount } from 'svelte';

	const user = $derived(userProvider.user);

	onMount(() => {
		if (!user) {
			goto('/welcome');
		} else {
			goto('/home');
		}
	});
</script>
