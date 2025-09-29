POS = {"good","great","love","like","awesome","happy"}
NEG = {"bad","terrible","hate","sad","awful","angry"}

def score(words: list[str]) -> int:
    """+1 per POS, -1 per NEG, 0 otherwise."""
    return sum((w in POS) - (w in NEG) for w in words)