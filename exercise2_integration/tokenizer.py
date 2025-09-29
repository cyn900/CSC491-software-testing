import re

def tokenize(text: str) -> list[str]:
    """Very simple word tokenizer."""
    return re.findall(r"[A-Za-z']+", text.lower())