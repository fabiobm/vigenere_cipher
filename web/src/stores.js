import { derived, writable } from 'svelte/store'

export const alphabetOption = writable('lowercase')
export const alphabetIncludeDigits = writable(false)
export const alphabetIsChar = writable(true)
export const alphabetExtra = writable('')
export const alphabetCharacters = writable('')
export const alphabetCharactersPattern = writable('')

export const alphabet = derived([alphabetOption, alphabetIncludeDigits, alphabetIsChar, alphabetExtra], ($option, $includeDigits, $chars, $extra) => ({
		option: $option,
		includeDigits: $includeDigits,
		chars: $chars,
		extra: $extra
	})
)

export const key = writable('')

export const message = writable('')

export const transform = writable('encode')

export const parameters = derived(
	[alphabetCharacters, alphabetCharactersPattern, alphabetIsChar, key, message, transform],
	([$characters, $pattern, $chars, $key, $message, $transform]) => {
		const regex = new RegExp(`^${$pattern}$`, 'm')

		return {
			alphabet: $chars ? $characters : $characters.trim().split(' '),
			key: $chars ? $key : $key.trim().split(' '),
			message: $chars ? $message : $message.trim().split(' '),
			encode: $transform === 'encode',
			valid: $characters && $key && $message && regex.test($key) && regex.test($message)
		}
	}
)
