# from package.numbers import sum_even_nums
# from package.words import filter_words_by_prefix

# from package import numbers, words
# import package.numbers
# import package.words

import package

nums = [1, 2, 3, 4]
print(package.numbers.sum_even_nums(nums))

prefix = 'hell'
words = ['hello world', 'hell', 'hello python', 'go to hell']
print(package.words.filter_words_by_prefix(words, prefix))

