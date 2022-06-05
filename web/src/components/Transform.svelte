<script>
	import { transform } from '../stores.js'
	import RadioButtonGroup from './RadioButtonGroup.svelte'
	
	const options = [
		{ label: 'Encode', value: 'encode' },
		{ label: 'Decode', value: 'decode' }
	]	
</script>

<style>
	fieldset > div {
		user-select: none;
		-webkit-user-select: none;
	}
</style>

<h2>
	Transform
</h2>

<p>
	Choose whether you want to encode or decode the message
</p>

<fieldset name="transform">
	<legend>
		transform
	</legend>

	<div>
		<RadioButtonGroup items={options} group={transform} />
	</div>
</fieldset>
