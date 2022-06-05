<script>
	import {
		alphabetOption,
		alphabetIncludeDigits as includeDigits,
		alphabetIsChar as chars,
		alphabetExtra as extra,
		alphabetCharacters as characters,
		alphabetCharactersPattern as pattern,
	} from '../stores.js'
	import { createPattern } from '../utils.js'
	import RadioButtonGroup from './RadioButtonGroup.svelte'

	const options = {
		lowercase: {
			label: 'Lowercase Latin alphabet',
			characters: 'abcdefghijklmnopqrstuvwxyz',
			pattern: 'a-z'
		},
		uppercase: {
			label: 'Uppercase Latin alphabet',
			characters: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
			pattern: 'A-Z'
		},
		lowercaseUppercase: {
			label: 'Lowercase and uppercase Latin alphabet',
			characters: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
			pattern: 'a-zA-Z'
		},
		digits: {
			label: 'Digits',
			characters: '0123456789',
			pattern: '0-9'
		},
		custom: {
			label: 'Custom',
			characters: ''
		}
	}
	

	$: custom = $alphabetOption === 'custom'
	
	$: {
		$characters = [...new Set(custom && !$chars
			? $extra.split(' ')
			: (options[$alphabetOption]?.characters ?? '') +
				($includeDigits ? options.digits.characters : '') +
				$extra
		)].join(custom && !$chars ? ' ' : '')

		$pattern = createPattern(options[$alphabetOption]?.pattern, $extra, $includeDigits, $chars)
	}

	let prevIncludeDigits = false, prevChars = false

	$: if (!custom) {
		prevChars = $chars
		$chars = true
	} else if ($chars && !prevChars) {
		$chars = false
		prevChars = true
	}
	
	$: if ($alphabetOption === 'digits' || custom) {
		prevIncludeDigits = $includeDigits
		$includeDigits = false
	} else if (!$includeDigits && prevIncludeDigits) {
		$includeDigits = true
		prevIncludeDigits = false
	}

	let showCharacters = false
</script>

<style>
	fieldset > div:last-child {
		flex-direction: column;
	}

	.alphabetOptionsContainer {
		display: flex;
		flex-direction: column;
		user-select: none;
		-webkit-user-select: none;
	}

	.customIsCharsContainer {
		padding-left: 2rem;
		user-select: none;
		-webkit-user-select: none;
	}

	.includeDigitsContainer {
		display: flex;
		align-items: center;
		margin-top: 1rem;
	}

	.extraCharsContainer {
		display: flex;
		flex-direction: column;
	}

	input:disabled + label {
		color: rgba(0, 0, 0, 0.25);
	}

	input[type="checkbox"] + label {
		padding-left: 0.8rem;
	}

	.charactersContainer.hidden {
		display: none
	}

	.charactersContainer > h4 {
		cursor: pointer;
		user-select: none;
		-webkit-user-select: none;
	}

	.charactersContainer > pre {
		display: none;
	}

	.charactersContainer > pre.showCharacters {
		display: block;
	}
</style>

<h2>
	Alphabet
</h2>

<p>
	Choose the set of valid characters (or even custom words)
</p>

<fieldset name="alphabet">
	<legend>
		alphabet
	</legend>

	<div class="alphabetOptionsContainer">
		<RadioButtonGroup items={Object.entries(options).map(([value, { label }]) => ({ label, value }))} group={alphabetOption} />
	</div>

	{#if custom}
		<div class="customIsCharsContainer">
			<RadioButtonGroup items={[ { label: 'Characters', value: true }, { label: 'Words', value: false }]} group={chars} />
		</div>
	{/if}
	
	<div class="includeDigitsContainer">
		<input type="checkbox" name="includeDigits" id="includeDigits" bind:checked={$includeDigits} disabled="{!$alphabetOption || $alphabetOption === 'digits' || custom}" />
		<label for="includeDigits">Include digits</label>
	</div>
	
	<div class="extraCharsContainer">
		<label for="extra">
			<h4>
				{custom ? 'Custom' : 'Extra'}
				{($alphabetOption !== 'custom' || $chars) ? 'characters' : 'words'}
			</h4>

			<p>
				{#if custom}
					Specify the custom {$chars ? 'characters' : 'words'} below,
					{$chars ? 'without any spaces or separators' : 'separated by a whitespace'}.
					Repeated {$chars ? 'characters' : 'words'} will only be counted once
				{:else}
					Optionally, add extra characters in the field below,
					without any spaces or separators.
					Repeated characters will only be counted once
				{/if}
			</p>
		</label>
		{#if $alphabetOption !== 'custom'}
			<input type="text" name="extra" id="extra" bind:value={$extra} />
		{:else}
			<textarea name="extra" id="extra" bind:value={$extra} />
		{/if}
	</div>		
</fieldset>

<div class="charactersContainer" class:hidden={custom}>
	<h4 on:click={() => showCharacters = !showCharacters}>
		{#if showCharacters}
			<span>&#9650;</span> Hide
		{:else}
			<span>&#9660;</span> Show
		{/if}
		valid {$chars ? 'characters' : 'words'}
	</h4>
	
	<pre class:showCharacters>{$characters}</pre>
</div>
