def filter_words_by_prefix(words, prefix):
    return list(filter(lambda x: x.startswith(prefix), words))
