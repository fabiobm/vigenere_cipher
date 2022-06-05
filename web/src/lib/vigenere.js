// @ts-check

/**
 * Transforms the text using the Vigenère cipher with the provided alphabet.
 * 
 * If the alphabet is composed of characters, it should be one string with the
 * concatenated characters, and the text and key should also be strings. If the
 * alphabet is composed of words, it should be an array of the words, and the
 * text and key should also be arrays.
 *
 * @param {string | string[]} text
 * @param {string | string[]} key
 * @param {string | string[]} alphabet
 * @param {boolean} [decrypting=false] a flag to indicate whether the transformation is to decrypt or encrypt
 * @return {string | string[]} 
 */
export function transform(text, key, alphabet, decrypting = false) {
    if (typeof alphabet !== 'string' && !Array.isArray(alphabet)) {
        throw new Error('Alphabet must be a string or list of strings')
    }

    if (new Set([...alphabet]).size < alphabet.length) {
        throw new Error('Alphabet must not have duplicated symbols')
    }

    if (key === '' || Array.isArray(key) && key.length === 0) {
        throw new Error('Key must not be empty')
    }

    if (typeof key !== 'string' && !Array.isArray(key)) {
        throw new Error('Key must be a string or a list of strings')
    }

    if (typeof text !== 'string' && !Array.isArray(text)) {
        throw new Error('Text must be a string or a list of strings')
    }

    const transformed = []
    let i = 0
    for (const symbol of [...text]) {
        const symbolIdx = alphabet.indexOf(symbol)
        if (symbolIdx === -1) {
            throw new Error('Symbols in text must be in the alphabet')
        }

        const keySymbolIdx = alphabet.indexOf(key[i % key.length])
        if (keySymbolIdx === -1) {
            throw new Error('Symbols in key must be in the alphabet')
        }

        let idx = (
            symbolIdx + (!decrypting ? keySymbolIdx : -keySymbolIdx)
        ) % alphabet.length
        if (idx < 0) idx += alphabet.length

        transformed.push(alphabet[idx])
        i++
    }

    return Array.isArray(key) ? transformed : transformed.join('')
}
