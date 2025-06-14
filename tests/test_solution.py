import pytest
from solution import Solution, TextProcessor


@pytest.fixture
def solver():
    return Solution()


# -------------------------
# TextProcessor unit tests
# -------------------------

def test_normalize_strips_and_lowercases():
    txt = "   Hello WORLD  "
    processor = TextProcessor(txt)
    assert processor.normalize() == "hello world"


def test_remove_punctuation_defaults():
    txt = "Wow! (This)—is: great?"
    processor = TextProcessor(txt)
    cleaned = processor.remove_punctuation("wow! (this)—is: great?")
    # default punctuation includes ! () — : ?
    assert cleaned == "wow thisis great"


def test_remove_punctuation_custom():
    txt = "a+b=c; d*e=f"
    proc = TextProcessor(txt, punctuation={"+", "=", "*"})
    # only +, =, * should be stripped; semicolon remains
    assert proc.remove_punctuation(txt) == "ab c; de f"


def test_tokenize_collapses_whitespace():
    proc = TextProcessor("")
    tokens = proc.tokenize("one   two\tthree\nfour")
    assert tokens == ["one", "two", "three", "four"]


def test_count_frequencies_and_get_top_n():
    tokens = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    proc = TextProcessor("")
    counts = proc.count_frequencies(tokens)
    assert counts == {"apple": 3, "banana": 2, "cherry": 1}

    # top_n=None returns all sorted
    top_all = proc.get_top_n(counts)
    assert top_all == [("apple", 3), ("banana", 2), ("cherry", 1)]

    # top_n=2 returns only first two
    top_two = proc.get_top_n(counts, n=2)
    assert top_two == [("apple", 3), ("banana", 2)]

    # top_n=0 returns empty list
    assert proc.get_top_n(counts, n=0) == []


# -----------------------------------
# Solution.word_frequency_counter tests
# -----------------------------------

def test_simple_sentence(solver):
    text = "hello world hello"
    assert solver.word_frequency_counter(text) == [("hello", 2), ("world", 1)]


def test_case_insensitivity_and_default_punctuation(solver):
    text = "The Cat, the hat?"
    result = solver.word_frequency_counter(text)
    # order is deterministic since counts differ
    assert result == [("the", 2), ("cat", 1), ("hat", 1)]


def test_punctuation_and_apostrophes(solver):
    text = "Isn't it amazing? Amazing, truly!"
    result = solver.word_frequency_counter(text)
    # apostrophe removed -> isnt
    assert dict(result) == {"isnt": 1, "it": 1, "amazing": 2, "truly": 1}
    # and sorted by frequency
    assert result[0] == ("amazing", 2)


def test_hyphenated_words_become_one_token(solver):
    text = "state-of-the-art design is state of art"
    # default punctuation set includes '-'
    result = solver.word_frequency_counter(text)
    # "stateoftheart" appears once, and "state", "of", "art" appear once each
    counts = dict(result)
    assert counts["stateoftheart"] == 1
    assert counts["state"] == 1 and counts["of"] == 1 and counts["art"] == 1


def test_numeric_tokens_and_top_n(solver):
    text = "123 456 123 test 456 456"
    # top_n=2 should pick 456 (3), then 123 (2)
    top2 = solver.word_frequency_counter(text, top_n=2)
    assert top2 == [("456", 3), ("123", 2)]


def test_whitespace_only_and_no_alphanum(solver):
    # only spaces
    assert solver.word_frequency_counter("     ") == []
    # only punctuation
    assert solver.word_frequency_counter(".,;!?'-") == []


def test_large_input_performance(solver):
    # repeats "foo bar " 10_000 times → 20_000 tokens
    text = "foo bar " * 10_000
    result = solver.word_frequency_counter(text)
    assert result == [("foo", 10_000), ("bar", 10_000)]


def test_non_string_input_raises_type_error(solver):
    with pytest.raises(TypeError):
        solver.word_frequency_counter(12345)
