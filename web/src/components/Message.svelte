<script>
	import { alphabetCharactersPattern as pattern, alphabetIsChar as chars, message } from '../stores.js'	
</script>

<h2>
	Message
</h2>

<p>
	Type the message (composed of the valid {$chars ? 'characters' : 'words'} above)
	to be encoded or decoded.
	{$chars ? '' : 'The words must be separated by whitespace'}
</p>

<fieldset name="message">
	<legend>
		message
	</legend>

	<input type="text" bind:value={$message} pattern={$pattern} placeholder=" " required />
	<span class="error">Check if the {$chars ? 'characters' : 'words'} are valid</span>
</fieldset>
