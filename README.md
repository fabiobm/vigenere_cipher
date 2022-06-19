# Vigenère Cipher

Python and JS implementations of the
[Vigenère Cipher](https://en.wikipedia.org/wiki/Vigenère_cipher)

## Python

The dependencies for the Python version are mostly formatting-related, and can
be installed with `pip install -r requirements.txt`.

The implementation is all in the [vigenere.py](vigenere.py) file; it can be
used by importing (e.g.: `from vigenere import Vigenere`) and then
instantiating the class (`v = new Vigenere()`) and using its `encrypt` and
`decrypt` methods. The parameters are documented in the source code.

The [test_vigenere.py](test_vigenere.py) file contains the unit tests for the
implementation and can be run with `python3 -m unittest test_vigenere.py`.

## JS

The cipher itself is implemented in pure JS in the
[vigenere.js](web/src/lib/vigenere.js) file, from which the `transform`
function can be imported and used. The parameters are documented in the source
code.

There's also a web app
(available [here](https://fabiobm.github.io/vigenere_cipher/)) with an
interface for applying the cipher, implemented in Svelte. To run this app,
first install the dependencies with `npm i` then use the dev server with
`npm run dev`, or use `npm run build` to generate the bundle or
`npm run preview` to better test it.
