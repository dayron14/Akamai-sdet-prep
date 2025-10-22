import pytest
from monday_anagam import are_we_anagrams  # assuming your function is in anagrams.py


class TestAreAnagrams:

    def test_basic_true_case(self):
        assert are_we_anagrams("listen", "silent") is True

    def test_basic_false_case(self):
        assert are_we_anagrams("hello", "world") is False

    def test_ignore_case_and_spaces(self):
        assert are_we_anagrams("Dormitory", "Dirty room") is True

    def test_with_extra_spaces(self):
        assert are_we_anagrams("The eyes ", "They see") is True

    def test_empty_strings(self):
        assert are_we_anagrams("", "") is True

    def test_partial_match(self):
        assert are_we_anagrams("abc", "ab") is False

@pytest.mark.parametrize("w1, w2, expected", [
    ("listen", "silent", True),
    ("evil", "vile", True),
    ("python", "typhon", True),
    ("apple", "papel", True),
    ("apple", "applf", False),
])
def test_multiple_anagrams(w1, w2, expected):
    assert are_we_anagrams(w1, w2) == expected
