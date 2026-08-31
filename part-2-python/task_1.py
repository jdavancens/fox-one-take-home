from collections import Counter
import string

def normalize(token: str) -> str:
    """Normalize a token.

    Convert to lowercase, strip leading/trailing whitespace, strip leading/trailing punctuation.
    """
    return token.lower().strip().strip(string.punctuation)

def most_common_word(text: str, stopwords: set[str] | None = None) -> str | None:
    """Count normalized tokens, skip stop words, and return the winner.
    
    Tie-breaker: first word in list.
    """
    if text == '':
        return None


    if stopwords is None:
        stopwords = set[str]()

    stopwords_norm = {normalize(x) for x in stopwords}

    tokens = []
    
    for token in text.split():
        token_norm = normalize(token)
        if token_norm not in stopwords_norm and token_norm != '':
            tokens.append(token_norm)

    if len(tokens) == 0:
        return None

    counter = Counter[str](tokens)

    return counter.most_common(1)[0][0]


