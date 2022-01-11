# __ALL__ = 

def sum_even_nums(nums):
    return list(filter(lambda score: score % 2 == 0, nums))


def sum_odd_nums(nums):
    return list(filter(lambda score: score % 2 == 1, nums))
