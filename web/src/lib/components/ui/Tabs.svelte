<script lang="ts">
	import type { Component } from 'svelte';
	import { Tabs } from 'bits-ui';

	interface Props {
		value?: string;
		tabs: { value: string; Widget: Component; label: string }[];
	}

	let { value = $bindable(), tabs }: Props = $props();
</script>

<Tabs.Root bind:value>
	<Tabs.List class="mb-2 flex justify-center space-x-1">
		{#each tabs as tab}
			<Tabs.Trigger
				value={tab.value}
				class={[
					'hover:bg-accent border px-2 py-1 transition',
					tab.value === value ? 'bg-accent' : ''
				]}
			>
				<span>{tab.label}</span>
			</Tabs.Trigger>
		{/each}
	</Tabs.List>

	{#each tabs as tab}
		<Tabs.Content value={tab.value}>
			<tab.Widget />
		</Tabs.Content>
	{/each}
</Tabs.Root>
