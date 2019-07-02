# 832. Flipping an Image

# class Solution:


def flipAndInvertImage(self, A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    return [[1 ^ i for i in row[::-1]] for row in A]


if __name__ == "__main":

    A = [1, 2, 3, 4]

    print(flipAndInvertImage(A))
