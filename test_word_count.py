from word_count import word_count


def test_simple_count():
    test_string = "This is a test string"
    assert word_count(test_string) == 5


def test_simple_count2():
    test_string = "hello"
    assert word_count(test_string) == 1


def test_empty_string():
    test_string = ""
    assert word_count(test_string) == 0