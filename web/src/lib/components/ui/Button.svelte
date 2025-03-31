<script lang="ts">
	import { Button } from 'bits-ui';
	import type { Snippet } from 'svelte';

	interface Props {
		children: Snippet;
		type?: 'button' | 'submit' | 'reset';
		variant?: 'primary' | 'secondary' | 'tertiary';
		size?: 'small' | 'medium' | 'large';
		disabled?: boolean;
		loading?: boolean;
		icon?: string;
		iconPosition?: 'left' | 'right';
		onclick?: () => void;
	}

	let { onclick, children, type = 'button' }: Props = $props();
</script>

<Button.Root {type} {onclick}>
	{@render children()}
</Button.Root>
