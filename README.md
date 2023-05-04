# VarTrie

VarTrie is a Python package that provides a container class for storing a set of words and efficiently querying whether a given string is in the set or not. 

Instead of classic trie VarTrie allows to specify a set of valid forms for each character in the words. For example, if the character table contains the character "p" with the forms "p" and "P", then the words "python" and "Python" are both considered to be in the set.

## Installation

> NotImplementedError: VarTrie is not yet available on PyPI.

## Usage

### Creating a VarTrie object

To create a VarTrie object, you need to provide a set of words and a character table that specifies the valid forms for each character in the words. Here's an example:

```python
from vartrie import VarTrie

words = {'hello', 'world', 'python', 'pycon'}
char_table = {'p': {'p', 'P'}, 'y': {'y', 'Y'}}

trie = VarTrie(words, char_table)
```

This creates a VarTrie object containing the words "hello", "world", "python", and "pycon". The character table specifies that the characters "p" and "y" can take two forms: "p" or "P", and "y" or "Y", respectively.

### Checking if a string is in the set

To check whether a string is in the set of words, you can use the `in` operator:

```python
'python' in trie   # True
'PyCon' in trie    # True
'foobar' in trie   # False
```

Note that the `in` operator is case-insensitive, because of the character table.

## License

VarTrie is released under the MIT License. See LICENSE file for details.

## Contributing

If you have found a bug or have a feature request, please create an issue on GitHub. If you would like to contribute code, please fork the repository and submit a pull request.