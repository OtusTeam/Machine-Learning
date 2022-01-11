from numbers import sum_even_nums
from words import filter_words_by_prefix
import tests


nums = [1, 2, 3, 4]
print(sum_even_nums(nums))

prefix = 'hello'
words = ['hello world', 'hell', 'hello python', 'go to hell']
print(filter_words_by_prefix(words, prefix))

print(__name__)

print(tests.__name__)
