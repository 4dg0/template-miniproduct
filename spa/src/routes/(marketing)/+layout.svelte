<script lang="ts">
	let { children } = $props();
</script>

<div class="mx-auto min-h-screen max-w-[1280px] border-x">
	{@render children()}
</div>
