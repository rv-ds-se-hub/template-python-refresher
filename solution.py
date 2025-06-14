from typing import Iterable


class TextProcessor:
    def __init__(self, text: str, punctuation: Iterable[str] | None = None):
        """
        Args:
            text: Raw input text to process.
            punctuation: Iterable of punctuation characters to remove.
        """
        self.text = text
        # Default punctuation set if none provided
        default = ".,?!;:\"'()[]-"
        self.punctuation = set(punctuation) if punctuation is not None else set(default)

    def normalize(self) -> str:
        """Lowercase the text and strip surrounding whitespace."""
        # TODO: implement normalization
        raise NotImplementedError

    def remove_punctuation(self, text: str) -> str:
        """Strip all characters in self.punctuation from the text."""
        # TODO: implement punctuation removal
        raise NotImplementedError

    def tokenize(self, text: str) -> list[str]:
        """Split text into tokens on whitespace, collapsing multiple spaces."""
        # TODO: implement tokenization
        raise NotImplementedError

    def count_frequencies(self, tokens: list[str]) -> dict[str, int]:
        """Count how often each token appears."""
        # TODO: implement frequency counting
        raise NotImplementedError

    def get_top_n(
        self, counts: dict[str, int], n: int | None = None
    ) -> list[tuple[str, int]]:
        """
        Return a list of (word, count) sorted by count descending.
        If n is provided, return only the top n items.
        """
        # TODO: implement top-n extraction
        raise NotImplementedError


class Solution:
    def word_frequency_counter(
        self, text: str, top_n: int | None = None
    ) -> list[tuple[str, int]]:
        """
        Main entry point.
        """
        processor = TextProcessor(text)
        cleaned = processor.normalize()
        cleaned = processor.remove_punctuation(cleaned)
        tokens = processor.tokenize(cleaned)
        counts = processor.count_frequencies(tokens)
        return processor.get_top_n(counts, top_n)
