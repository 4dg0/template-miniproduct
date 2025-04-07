<script lang="ts">
	import { m } from '$lib/paraglide/messages';
	import { setLocale } from '$lib/paraglide/runtime';

	import { settingsProvider } from '$lib/providers/settings.svelte';
	import { Tween } from 'svelte/motion';

	let { children } = $props();
	const lang = $derived(settingsProvider.lang);

	let expanded = $state(false);
	const sidebarWidth = new Tween(100, { duration: 200 });
</script>

{#key lang}
	<div class="flex min-h-screen">
		<aside
			style:width={`${sidebarWidth.current}px`}
			class={[
				'min-h-screen flex-col justify-between overflow-hidden border-r p-4',
				'hidden lg:flex'
			]}
		>
			<div>
				<div class="flex justify-center">
					<button
						onclick={() => {
							if (expanded) {
								sidebarWidth.target = 150;
								expanded = false;
							} else {
								sidebarWidth.target = 300;
								expanded = true;
							}
						}}
					>
						O
					</button>
				</div>

				<nav>
					<a class="flex" href="/">{m.nav_home()}</a>
					<a class="flex" href="/sign-up">{m.nav_signUp()}</a>
					<a class="flex" href="/sign-in">{m.nav_signIn()}</a>
				</nav>
			</div>

			<ul>
				<li>
					<button
						class="border"
						onclick={() => {
							const newTheme = settingsProvider.theme === 'dark' ? 'light' : 'dark';
							localStorage.setItem('theme', newTheme);
							document.documentElement.classList.toggle('dark');
							settingsProvider.setTheme(newTheme);
						}}
					>
						theme
					</button>
				</li>
				<li>
					<button
						class="border"
						onclick={() => {
							const newLang = lang === 'ru' ? 'en' : 'ru';
							setLocale(newLang, { reload: false });
							settingsProvider.setLang(newLang);
						}}
					>
						{lang === 'ru' ? 'to <en>' : 'to <ru>'}
					</button>
				</li>
				<li>
					<a href="/profile">Profile</a>
				</li>
			</ul>
		</aside>

		<div class="flex flex-1 flex-col">
			<header>Header</header>

			<main class="flex-1">
				{@render children()}
			</main>

			<footer class="lg:hidden">
				<p>Footer</p>
			</footer>
		</div>
	</div>
{/key}
