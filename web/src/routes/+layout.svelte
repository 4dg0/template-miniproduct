<script lang="ts">
	import '../app.css';
	import { m } from '$lib/paraglide/messages';
	import { getLocale, setLocale } from '$lib/paraglide/runtime';

	let { children } = $props();
	const lang = getLocale();
</script>

<header>
	<a href="/auth">AUTH</a>

	<button
		class="border"
		onclick={() => {
			document.documentElement.classList.toggle('dark');
			console.log('toggle theme');
		}}
	>
		theme
	</button>

	<button
		class="border"
		onclick={() => {
			setLocale(lang === 'ru' ? 'en' : 'ru');
		}}
	>
		{lang === 'ru' ? 'to <en>' : 'to <ru>'}
	</button>
</header>

{@render children()}

<div>
	{m.hello_world({ name: '4dg0' })}
</div>
