from slugify_kit import slugify


def test_keeps_case_by_default():
    assert slugify("Hello World") == "Hello-World"


def test_lower_is_opt_in():
    assert slugify("Hello World", lower=True) == "hello-world"


def test_transliterates_unicode():
    assert slugify("Cr\u00e8me Br\u00fbl\u00e9e") == "Creme-Brulee"
