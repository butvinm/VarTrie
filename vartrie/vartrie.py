from typing import Container

Node = dict[str, "Node"]

END = "_end_"


class VarTrie(Container[str]):
    """
    A variable-forms trie for efficiently storing and retrieving a set of words.

    The trie is constructed using a set of words and a character table, which maps each letter
    to a set of its possible forms. For example, the letter 'a' may have uppercase and lowercase
    forms, and accented forms in other languages.

    The trie can then be used to efficiently test whether a given word is in the set of words.

    Example:
        words = {'apple', 'banana', 'orange', 'pear'}
        char_table = {'a': {'a', 'A', 'á', 'Á'}, 'e': {'e', 'é', 'É'}, ...}
        trie = VarTrie(words, char_table)
        'banAnÁ' in trie  # True
        'kiwi' in trie   # False
    """

    def __init__(self, words: set[str], char_table: dict[str, set[str]]) -> None:
        """
        Constructs a new VarTrie from a set of words and a character table.

        Args:
            words: A set of words to store in the trie.
            char_table: A dict mapping each letter to a set of its possible forms.
        """

        self.root: Node = self._build(words, char_table)

    def _build_word(self, root: Node, word: str, char_table: dict[str, set[str]]) -> Node:
        """
        Recursively builds a node in the trie for a given word.

        First, node for the first letter of the word built recursively. 
        Then, the remaining letters are added as copy of the first letter's node. 

        Args:
            root: The root node of the trie subtree to build on.
            word: The word to add to the trie.
            char_table: A dict mapping each letter to a set of its possible forms.

        Returns:
            The node in the trie corresponding to the last letter of the word.
        """

        if not word:
            root[END] = {}
            return root

        current_dict = root

        init_letter = word[0]
        forms = char_table.get(init_letter, {init_letter}).copy()

        letter_node = self._build_word(
            current_dict.setdefault(forms.pop(), {}),
            word[1:],
            char_table
        )

        for form in forms:
            current_dict[form] = letter_node

        return current_dict

    def _build(self, words: set[str], char_table: dict[str, set[str]]) -> Node:
        """
        Builds the entire trie from a set of words and a character table.

        Args:
            words: A set of words to store in the trie.
            char_table: A dict mapping each letter to a set of its possible forms.

        Returns:
            The root node of the trie.
        """

        root: Node = dict()
        for word in words:
            self._build_word(root, word, char_table)

        return root

    def __contains__(self, word: object) -> bool:
        """
        Tests whether a given word is in the set of words stored in the trie.

        Args:
            word: The word to test.

        Returns:
            True if the word is in the trie, False otherwise.
        """

        if not isinstance(word, str):
            raise TypeError('word must be str, not ' + type(word).__name__)

        current_dict = self.root
        for letter in word:
            if not letter in current_dict:
                return False

            current_dict = current_dict[letter]

        return END in current_dict
