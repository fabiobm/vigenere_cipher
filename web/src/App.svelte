<script>
    import Alphabet from './components/Alphabet.svelte'
    import Key from './components/Key.svelte'
    import Message from './components/Message.svelte'
    import Transform from './components/Transform.svelte'
    import Output from './components/Output.svelte'
</script>

<style>
    :root {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
        Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        font-size: 62.5%;
    }

    header {
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    }

    h1 {
        padding: 1.2rem;
        margin: 0;
    }
    
    main {
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }

    h1, main {
        max-width: 540px;
        padding-left: 4rem;
        padding-right: 4rem;
        margin: auto;
    }

    @media (max-width: 320px) {
        h1 {
            font-size: 1.5em;
        }

        :global(h2) {
            font-size: 1.2em;
        }

        :global(input[type="text"], textarea, pre) {
            max-width: 100%;
        }
    }

    @media (min-width: 970px) {
        h1, main {
            max-width: 900px;
            padding-left: 8rem;
            padding-right: 8rem;
        }

        :global(input[type="text"], textarea, pre) {
            max-width: 50%;
        }
    }

    :global(html), :global(body) {
        width: 100%;
        height: 100%;
    }

    :global(body) {
        margin: 0;
        padding: 0;
        font-size: 1.6rem;
    }

    :global(h2) {
        margin-top: 4rem;
    }

    :global(fieldset) {
        display: flex;
        flex-direction: column;
        border: none;
        padding: 0;
        margin: 0;
    }
    
    :global(fieldset > legend) {
        display: none;
    }

    :global(input[type="text"], textarea) {
        border: 1px solid #ccc;
        border-radius: 4px;
        padding: 0.4rem 0.8rem;
        margin-left: 0;
    }

    :global(input[type="text"], textarea, pre) {
        max-width: 80%;
    }

    :global(input[type="text"]) {
        height: 2rem;
        vertical-align: middle;
    }

    :global(input[type="text"]:not(:focus):not(:placeholder-shown):invalid) {
		border: 1px solid rgba(241, 120, 120, 0.75);
    }

    :global(.error) {
        visibility: hidden;
		color: rgb(190, 73, 73);
		font-size: 0.75em;
        padding-top: 0.4rem;
    }

    :global(input[type="text"]:not(:placeholder-shown):invalid + .error) {
        visibility: visible;
    }

    :global(pre) {
		border: 1px dashed black;
		border-radius: 3px;
		padding: 0.8rem;
        overflow: scroll;
        white-space: nowrap;
    }
</style>

<header>
    <h1>Vigènere Cipher</h1>
</header>

<main>
    <p>
        Transform (encode or decode) text using the
        <a href="https://en.wikipedia.org/wiki/Vigenère_cipher" target="_blank">Vigenère Cipher</a>,
        which shuffles the message based on the key phrase.
    </p>

    <p>
        This version not only works with the regular Latin alphabet,
        it also allows using digits, other custom characters or even a list of words.
        Select below the alphabet option, the key and the message and see the output
        of the encoding/decoding.
    </p>

    <Alphabet />
    <Key />
    <Message />
    <Transform />
    <Output />
</main>
