from slugify_kit import slugify


def test_lowercases_by_default():
    assert slugify("Hello World") == "hello-world"


def test_transliterates_unicode():
    assert slugify("Crème Brûlée") == "creme-brulee"


def test_max_len_trims_on_separator():
    assert slugify("one two three", max_len=7) == "one-two"
