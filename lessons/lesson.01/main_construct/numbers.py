def sum_even_nums(nums):
    return list(filter(lambda score: score % 2 == 0, nums))


# print(sum_even_nums(''))
# print(sum_even_nums([1]))
# print(sum_even_nums([1, 3]))

print(__name__)

if __name__ == '__main__':
    print(__name__)
    print(sum_even_nums(''))
    print(sum_even_nums([1]))
    print(sum_even_nums([1, 3]))
