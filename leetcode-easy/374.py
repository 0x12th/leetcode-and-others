# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


def guess_number(n: int) -> int:
    left, right = 0, n

    while left <= right:
        mid = (left + right) // 2
        match guess(mid):
            case -1:
                right = mid - 1
            case 1:
                left = mid + 1
            case _:
                return mid