import string

chars_to_remove = set([*string.whitespace, *string.punctuation])

def create_anagram_key(word: str) -> str:
    word_norm = [char for char in word.lower() if char not in chars_to_remove]
    return "".join(sorted(word_norm))


def group_anagrams(words: list[str]) -> list[list[str]]:
    anagrams: dict[str, list[str]] = {}

    for word in words:
        anagram_key = create_anagram_key(word)

        if anagram_key in anagrams:
            anagrams[anagram_key].append(word)
        else:
            anagrams[anagram_key] = [word]

    return list(anagrams.values())