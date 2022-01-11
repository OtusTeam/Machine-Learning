# from folder.numbers import sum_even_nums, sum_odd_nums as odds
from folder.numbers import *
import folder.numbers
from folder.words import filter_words_by_prefix

nums = [1, 2, 3, 4]
print(folder.numbers.sum_even_nums(nums))

prefix = 'hello'
words = ['hello world', 'hell', 'hello python', 'go to hell']
print(filter_words_by_prefix(words, prefix))
