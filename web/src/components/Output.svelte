<script>
	import { transform } from '../lib/vigenere.js'
	import { parameters } from '../stores'

	$: output = $parameters.valid
		? (() => {
			try {
				return transform($parameters.message, $parameters.key, $parameters.alphabet, !$parameters.encode)
			} catch (e) {
				console.error('Error applying Vigenère cipher:', e)
				return ''
			}
		})()
		: ''

	function copy() {
		const textarea = document.createElement('textarea')
		document.body.appendChild(textarea)

		textarea.value = Array.isArray(output) ? output.join(' ') : output
		textarea.select()
		
		document.execCommand('copy')
		document.body.removeChild(textarea)
	}
</script>

<style>
	.notAvailable {
		opacity: 30%;
	}

	div {
		display: flex;
		flex-direction: column;
	}

	button {
		display: flex;
		align-items: center;
		justify-content: center;
		-webkit-appearance: none;
		max-width: 6rem;
		background-color: #eee;
		box-shadow: none;
		border: 2px solid #ccc;
		margin: 0;
		border-radius: 4px;
		height: 3rem;
		cursor: pointer;
		font-size: 0.8em;
	}

	button:hover {
		background-color: #ccc;
	}

	button:active {
		border-color: black;
		color: black;
	}
</style>

<h2>
	Output
</h2>

<div>
	{#if $parameters.valid && (Array.isArray(output) ? output.length : output)}
		<pre>{Array.isArray(output) ? output.join(' ') : output}</pre>
		<button on:click={copy}>copy</button>
	{:else}
		<pre class="notAvailable">&mdash;</pre>
	{/if}
</div>
