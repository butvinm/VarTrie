import pytest

from vartrie import VarTrie


def test_contains():
    words = {"apple", "banana", "orange", "pear", "apricot"}
    char_table = {"a": {"a", "A", "á", "Á"}, "e": {"e", "é", "É"}}
    trie = VarTrie(words, char_table)
    assert "banAnÁ" in trie
    assert "ÁpplÉ" in trie
    assert "apricot" in trie
    assert "kiwi" not in trie


def test_non_string():
    words = {"apple", "banana", "orange", "pear", "apricot"}
    char_table = {"a": {"a", "A", "á", "Á"}, "e": {"e", "é", "É"}}
    trie = VarTrie(words, char_table)
    with pytest.raises(TypeError):
        assert 42 in trie
    with pytest.raises(TypeError):
        assert [1, 2, 3] in trie


def test_empty_trie():
    words: set[str] = set()
    char_table = {"a": {"a", "A", "á", "Á"}, "e": {"e", "é", "É"}}
    trie = VarTrie(words, char_table)
    assert "" not in trie
    assert "apple" not in trie


def test_single_word_trie():
    words = {"apple"}
    char_table = {"a": {"a", "A", "á", "Á"}, "e": {"e", "é", "É"}}
    trie = VarTrie(words, char_table)
    assert "apple" in trie
    assert "banana" not in trie


def test_empty_char_table():
    words = {"apple", "banana", "orange", "pear"}
    char_table = {}
    trie = VarTrie(words, char_table)
    assert "apple" in trie
    assert "banana" in trie


def test_build():
    words = {"apple", "banana", "orange", "pear", "apricot"}
    char_table = {"a": {"a", "A", "á", "Á"}, "e": {"e", "é", "É"}}
    trie = VarTrie(words, char_table)

    assert set(trie.root) == {"a", "A", "á", "Á", "b", "o", "p"}
    assert set(trie.root["a"]) == {"p"}
    assert set(trie.root["a"]["p"]) == {"p", "r"}
    assert set(trie.root["a"]["p"]["p"]) == {"l"}
    assert set(trie.root["a"]["p"]["p"]["l"]) == {"e", "é", "É"}