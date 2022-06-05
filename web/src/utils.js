export function createPattern(base = '', extra = '', includeDigits = false, isChars = true) {
    const specialChars = '\\.[](){}^$+*?:|<>='

    if (isChars) {
        const escapedExtra = [...new Set(extra.split(''))]
            .sort((a, b) => a === '-' ? 1 : b === '-' ? -1 : 0)
            .map(c => '\[]'.includes(c) ? `\\${c}` : c)
            .join('')

        return `[${base}${includeDigits ? '\\d' : ''}${escapedExtra}]+`
    }

    const escapedWords = [...new Set(extra.split(' '))]
        .map(w => w.split('').map(c => specialChars.includes(c) ? `\\${c}` : c).join(''))
        .join('|')

    return `(${escapedWords})+(${escapedWords}|\\s)*`
}
