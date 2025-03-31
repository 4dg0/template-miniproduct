<script lang="ts">
	let { children } = $props();
</script>

<main class="bg-card border-card mx-auto max-w-2xl rounded-lg border p-4 shadow-md">
	{@render children()}
</main>
