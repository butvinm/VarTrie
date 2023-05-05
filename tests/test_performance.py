import random
import string
from typing import Any, Callable
import pytest
from vartrie import VarTrie


@pytest.fixture
def words():
    # Generate a set of 10,000 random words
    words = set(''.join(random.choices(string.ascii_lowercase, k=10)) for _ in range(10000))
    return words


@pytest.fixture
def char_table():
    # Define a simple character table with no variations
    return {char: {char} for char in string.ascii_lowercase}


def test_build_speed(words: set[str], char_table: set[str], benchmark: Callable[..., Any]):
    # Measure the time it takes to build the VarTrie
    benchmark(VarTrie, words, char_table)


def test_search_speed(words: set[str], char_table: dict[str, set[str]], benchmark: Callable[..., Any]):
    # Build a VarTrie and measure the time it takes to search for all words
    trie = VarTrie(words, char_table)
    benchmark(trie.__contains__, 'aardvark')
