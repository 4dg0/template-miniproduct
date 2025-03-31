<script lang="ts">
	import Button from '$lib/components/ui/Button.svelte';
</script>

<div>
	<form
		onsubmit={(e) => {
			e.preventDefault();
			console.log('Form submitted');
		}}
		class="flex flex-col gap-4"
	>
		<input class="bg-background" type="email" placeholder="Email" />
		<input class="bg-background" type="password" placeholder="Password" />

		<Button type="submit">Submit</Button>
	</form>
</div>
