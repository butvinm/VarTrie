# VarTrie

VarTrie is a python package that provides a prefix trie for words with letters that have variable forms.

VarTrie (Variable Trie) allows searching for words in different forms. In some scenarios, this can be useful to filter out inappropriate words, to fine transliterated or obfuscated words, etc.

## Installation

You can install VarTrie using pip.

```bash
pip install VarTrie
```

## Usage

Here is a simple example of how to use VarTrie.

```python
from vartrie import VarTrie

words = {'apple', 'banana', 'apricot'}
chars_table = {'a': {'á', '@-'}, 'e': {'e', 'é', 'É'}}
trie = VarTrie(chars_table, words)

trie.search('@-pplÉ')  # True
trie.search('apple')  # False (because 'a' is not in chars_table)

trie.search_prefix('báná')  # True

trie.insert('pear')
trie.search('pÉár')  # True
```

In this example, `words` is a set of words to be inserted into the trie, and `chars_table` is a dictionary that maps each letter to a set of its possible forms. For instance, `chars_table['a']` is a set of alternative forms of letter 'a', including 'á' and '@-'. If a letter is not in the `chars_table`, it is assumed to have only one form, itself.

To create a VarTrie object, we need to provide `chars_table` and `words` (optional). After creating a VarTrie object, we can search for words by calling `search` method with a word to be searched. We can also search for a prefix of a word by calling `search_prefix` method with a prefix to be searched.


## Performance and space complexity

> more details will be added soon

For set of 47k words with chars_table of 26 letters with about 20 forms per letter, the trie build in 0.05 second, has 4000 nodes and takes 50kb as pickle file.

Searching of 47k obfuscated words takes 0.5 second. Search of 47k words not represented in the trie takes 1.5 second.

## Contributing

We welcome contributions! If you find any bugs or have any ideas for new features, please create an issue or a pull request on GitHub.

## License

VarTrie is released under the MIT License
