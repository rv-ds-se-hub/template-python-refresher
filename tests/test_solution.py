# tests/test_solution.py

import pytest

from ..solution import word_frequency_counter


def test_simple_sentence():
    """Tests a basic sentence with no punctuation or case issues."""
    text = "hello world hello"
    expected = [("hello", 2), ("world", 1)]
    assert word_frequency_counter(text) == expected


def test_case_insensitivity():
    """Tests that the function correctly handles mixed case."""
    text = "The Cat in the Hat"
    result = word_frequency_counter(text)
    # Convert to dict for order-insensitive comparison
    result_dict = dict(result)
    expected_dict = {"the": 2, "cat": 1, "in": 1, "hat": 1}
    assert result_dict == expected_dict
    assert len(result) == 4  # Ensure no extra words


def test_punctuation_removal():
    """Tests that punctuation is correctly removed."""
    text = "Wow! This is great, isn't it?"
    result = word_frequency_counter(text)
    result_dict = dict(result)
    expected_dict = {"wow": 1, "this": 1, "is": 1, "great": 1, "isnt": 1, "it": 1}
    assert result_dict == expected_dict


def test_empty_string():
    """Tests behavior with an empty string input."""
    assert word_frequency_counter("") == []


def test_string_with_only_punctuation():
    """Tests a string containing only punctuation."""
    assert word_frequency_counter(".,?!'-") == []


def test_complex_example():
    """Tests a more complex sentence with mixed case and punctuation."""
    text = "The quick brown fox jumps over the lazy dog. The dog was not lazy."
    expected = [
        ("the", 3),
        ("dog", 2),
        ("lazy", 2),
        ("quick", 1),
        ("brown", 1),
        ("fox", 1),
        ("jumps", 1),
        ("over", 1),
        ("was", 1),
        ("not", 1),
    ]
    assert word_frequency_counter(text) == expected


def test_input_type_error():
    """Tests that a non-string input raises a TypeError."""
    with pytest.raises(TypeError):
        word_frequency_counter(123)
