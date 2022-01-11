# 1. импортирование всего модуля
# import baskets
# import new_baskets

# import numbers

# nums = [1, 2, 3, 4, 5]
# even_nums = numbers.sum_even_nums(nums)
# print(even_nums)
# print(numbers.RELATIVE_PATH)

# 2. импортирование модуля с псевдонимом
# import baskets as bskt
# import numpy as np
# import pandas as pd

# import numbers as nums

# print(nums.sum_even_nums([1, 2, 3, 4]))


# 3. import basket
# from baskets import Basket, IncorrectValueNumber, test_function, RELATIVE_PATH, DIRECTORY, DIRECTORY
# from baskets import Basket as bt, IncorrectValueNumber as IVNumber

# from numbers import sum_even_nums, RELATIVE_PATH as RP

# print(RP)
# print(sum_even_nums([1, 2, 3, 4]))

# 4. импорт всего из модуля - импортирование лишнего, конфликты, нечитабельно
# from baskets import *
# from basket.main import Basket

from numbers import *

print(RELATIVE_PATH)
print(sum_even_nums([1, 2, 3, 4]))
