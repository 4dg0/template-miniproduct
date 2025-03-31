<script lang="ts">
	import '../app.css';
	import { m } from '$lib/paraglide/messages';
	import { getLocale, setLocale } from '$lib/paraglide/runtime';

	let { children } = $props();
	const lang = getLocale();
</script>

<div class="mx-auto min-h-screen max-w-[1280px] border-x p-4">
	<header>
		<a href="/sign-up">sign-up</a>
		<a href="/sign-in">sign-in</a>

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
</div>
