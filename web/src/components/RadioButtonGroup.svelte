<script>
	export let items, group
</script>

<style>
	label {
		padding-left: 0.4rem;
	}

	div {
		display: flex;
		align-items: center;
		justify-content: flex-start;
	}
</style>

{#each items as {value, label }}
	<div>
		<input type="radio" on:change value={value} id={value} bind:group={$group} />	
		<label for={value}>{label}</label>
	</div>
{/each}
