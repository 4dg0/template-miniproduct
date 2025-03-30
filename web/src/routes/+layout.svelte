<script lang="ts">
	import '../app.css';

	let { children } = $props();
</script>

<header>
	<button
		class="border"
		onclick={() => {
			document.documentElement.classList.toggle('dark');
			console.log('toggle theme');
		}}
	>
		theme
	</button>
</header>

{@render children()}
