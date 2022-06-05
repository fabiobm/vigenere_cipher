<script>
	import { alphabetCharactersPattern as pattern, alphabetIsChar as chars, key } from '../stores.js'
</script>

<h2>
	Key
</h2>

<p>
	Type a key (composed of the valid {$chars ? 'characters' : 'words'} above)
	to use for encoding or decoding the message.
	{$chars ? '' : 'The words must be separated by whitespace'}
</p>

<fieldset name="key">
	<legend>
		key
	</legend>

	<input type="text" bind:value={$key} pattern={$pattern} placeholder=" " required />
	<span class="error">Check if the {$chars ? 'characters' : 'words'} are valid</span>
</fieldset>
