from random import choice, choices, randint
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

import pytest

from vartrie import VarTrie


@pytest.fixture
def words():
    return {
        'apple', 'banana', 'apricot',
        'melon', 'mango', 'pineapple', 'pear', 'peach',
    }


@pytest.fixture
def chars_table():
    return {
        'a': {'á', '@-'}, 'e': {'e', 'é', 'É'},
        'm': {'m', 'M'}, 'p': {'p', 'P'},
    }


@pytest.fixture
def words_forms(words: set[str], chars_table: dict[str, set[str]]) -> set[str]:
    words_forms = set()
    for word in words:
        for _ in range(10):
            word_form = ''
            for char in word:
                if char not in chars_table:
                    word_form += char
                else:
                    word_form += choice(tuple(chars_table[char]))

            words_forms.add(word_form)

    return words_forms


@pytest.fixture
def words_prefixes(words: set[str], chars_table: dict[str, set[str]]) -> set[str]:
    words_prefixes = set()
    for word in words:
        for i in range(1, len(word)):
            prefix = word[:i]
            prefix_form = ''
            for char in prefix:
                if char not in chars_table:
                    prefix_form += char
                else:
                    prefix_form += choice(tuple(chars_table[char]))

            words_prefixes.add(prefix_form)

    return words_prefixes


@pytest.fixture
def not_existed_words(words_forms: set[str]):
    not_existed_words = set()
    while len(not_existed_words) < 20:
        word = ''.join(choices(
            ascii_lowercase + ascii_uppercase + digits + punctuation,
            k=randint(1, 10),
        ))
        if word not in words_forms:
            not_existed_words.add(word)

    return not_existed_words


@pytest.fixture
def trie(words: set[str], chars_table: dict[str, set[str]]) -> VarTrie:
    return VarTrie(chars_table, words)


@pytest.fixture
def trie_with_empty_chars_table(words: set[str]) -> VarTrie:
    return VarTrie({}, words)


@pytest.fixture
def empty_trie(chars_table) -> VarTrie:
    return VarTrie(chars_table)


def test_search(
    trie: VarTrie,
    words_forms: set[str],
    not_existed_words: set[str]
):
    for word in words_forms:
        assert trie.search(word)

    for word in not_existed_words:
        assert not trie.search(word)


def test_search_with_empty_chars_table(
    trie_with_empty_chars_table: VarTrie,
    words: set[str],
    not_existed_words: set[str],
):
    for word in words:
        assert trie_with_empty_chars_table.search(word)

    for word in not_existed_words:
        assert not trie_with_empty_chars_table.search(word)


def test_search_with_empty_trie(
    empty_trie: VarTrie,
    words_forms: set[str],
    not_existed_words: set[str],
):
    for word in words_forms:
        assert not empty_trie.search(word)

    for word in not_existed_words:
        assert not empty_trie.search(word)


def test_insert(
    empty_trie: VarTrie,
    words_forms: set[str],
):
    for word in words_forms:
        assert not empty_trie.search(word)

    for word in words_forms:
        empty_trie.insert(word)

    for word in words_forms:
        assert empty_trie.search(word)


def test_search_prefix(
    trie: VarTrie,
    words_prefixes: set[str],
):
    for prefix in words_prefixes:
        assert trie.search_prefix(prefix)
        assert not trie.search(prefix)
