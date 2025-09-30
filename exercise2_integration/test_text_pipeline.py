from text_pipeline import analyze
import pytest

def test_pipeline_positive():
    out = analyze("I love good food")
    assert out["words"] == ["I","love","good","food"]
    assert out["score"] == 2
    assert out["label"] == "pos"

def test_pipeline_negative_mixes():
    out = analyze("I love fries but hate the sauce")
    # 1 positive (love), 1 negative (hate) -> net 0
    assert out["score"] == 0
    assert out["label"] == "neu"

def test_pipeline_all_negative():
    out = analyze("awful bad terrible")
    assert out["label"] == "neg"

# TODO: Write a test case tht include captial letters and punctuation

# TODO: Write a test case that includes repeated words

# TODO: add the assertion checks
# def test_pipeline_unicode_emoji():
#     out = analyze("I LOVE THIS 😊👍 but the UI is bad 😡")

# TODO: fix analyze to reject non-string inputs
# def test_pipeline_rejects_non_string():
#     with pytest.raises(TypeError):
#         analyze(123) 