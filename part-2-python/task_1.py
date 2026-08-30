from collections import Counter
import string

def normalize(token: str) -> str:
    return token.lower().strip().strip(string.punctuation)

def most_common_word(text: str, stopwords: set[str] | None = None) -> str | None:
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


