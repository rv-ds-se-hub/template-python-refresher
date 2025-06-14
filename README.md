# Assignment 1: Text Processing with OOP in Python

## 🎯 Objective
Build a reusable, object-oriented text processing pipeline that can:
1. Normalize text
2. Remove configurable punctuation
3. Tokenize into words
4. Count word frequencies
5. Extract the top _n_ most common words (or all words if _n_ is omitted)

This will give you practice in designing classes, writing clean APIs, and handling edge cases beyond a simple script.

---

## 📋 Requirements

1. **`TextProcessor` class**  
   - **Initialization**  
     ```python
     def __init__(self, text: str, punctuation: Optional[Iterable[str]] = None):
         """
         :param text: raw input string
         :param punctuation: iterable of punctuation chars to strip (defaults to . , ? ! ; : " ' ( ) [ ] - )
         """
     ```
   - **Methods**  
     - `normalize() -> str`  
       Convert to lowercase, strip leading/trailing whitespace.
     - `remove_punctuation(text: str) -> str`  
       Remove _all_ characters in `self.punctuation`.
     - `tokenize(text: str) -> List[str]`  
       Split on whitespace (collapse multiple spaces).
     - `count_frequencies(tokens: List[str]) -> Dict[str, int]`  
       Build a word→count mapping.
     - `get_top_n(counts: Dict[str,int], n: Optional[int] = None) -> List[Tuple[str,int]]`  
       Return a list of `(word, count)` sorted by descending count. If `n` is given, return only the top _n_.

2. **`Solution` class**  
   - Method signature:
     ```python
     def word_frequency_counter(self, text: str, top_n: Optional[int] = None) -> List[Tuple[str,int]]:
         """
         Returns the list of (word, count) sorted by count desc.
         If top_n is provided, returns only the top N words.
         """
     ```
   - Should instantiate `TextProcessor` and chain its methods.

3. **Edge Cases**  
   - Empty or whitespace-only input
   - Text with no alphanumeric characters
   - Very large text inputs (efficiency matters)

4. **Code Quality**  
   - PEP8-compliant, descriptive docstrings
   - Meaningful variable names
   - No global variables
   - Each class/method does one thing

5. **Testing**  
   - A `tests/` directory is provided.
   - Run `make test` to verify your work.
   - You may add extra tests for your new features if you like.

---