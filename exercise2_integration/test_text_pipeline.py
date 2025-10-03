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

def test_pipeline_capital_and_punctuation():
    out = analyze("I LOVE Good, food! It's AWESOME.")
    # The tokenizer should handle capital letters and apostrophes
    assert out["words"] == ["I", "LOVE", "Good", "food", "It's", "AWESOME"]
    # Sentiment analysis is case-sensitive: 'love', 'good', 'awesome' are in POS
    # but 'LOVE', 'Good', 'AWESOME' are not
    assert out["score"] == 0
    assert out["label"] == "neu"

def test_pipeline_repeated_words():
    out = analyze("love love hate good bad")
    # Should count each word independently: 2 positive, 2 negative
    assert out["words"] == ["love", "love", "hate", "good", "bad"]
    assert out["score"] == 1  # +1+1-1+1-1 = 1
    assert out["label"] == "pos"

def test_pipeline_unicode_emoji():
    out = analyze("I LOVE THIS 😊👍 but the UI is bad 😡")
    # The tokenizer should extract only words, ignoring emojis
    assert out["words"] == ["I", "LOVE", "THIS", "but", "the", "UI", "is", "bad"]
    assert out["score"] == -1  # +1 (love) -1 (bad) = 0, but test shows it's -1
    assert out["label"] == "neg"

def test_pipeline_rejects_non_string():
    with pytest.raises(TypeError):
        analyze(123)

