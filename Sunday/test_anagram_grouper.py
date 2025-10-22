from anagram_grouper import anagram_grouper  # replace with your actual filename

def test_anagram_grouper_basic():
    input_words = ["bat", "tab", "tap", "pat", "cat"]
    expected_output = [["bat", "tab"], ["tap", "pat"], ["cat"]]

    # Because the order of groups or words within them might differ,
    # we can compare sets instead of lists for flexibility
    output = [set(group) for group in anagram_grouper(input_words)]
    expected = [set(group) for group in expected_output]

    assert all(group in output for group in expected)

def test_anagram_grouper_single_word():
    assert anagram_grouper(["hello"]) == [["hello"]]

def test_anagram_grouper_mixed_case():
    result = anagram_grouper(["Listen", "Silent", "Cat"])
    # Normalize to lowercase before comparing
    normalized = [set(word.lower() for word in group) for group in result]
    expected = [{"listen", "silent"}, {"cat"}]
    assert all(group in normalized for group in expected)

def test_anagram_grouper_empty_input():
    assert anagram_grouper([]) == []

