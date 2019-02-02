class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_32 = 2147483647
        min_32 = -2147483648

        if x > max_32 or x < min_32:
            return 0
        else:
            res = 0
            sign = (x>0) - (x<0)
            x = abs(x)
            while(x!=0):
                rem = x % 10
                x = x // 10
                res = res * 10 + rem
                if res > max_32 or res < min_32:
                    return 0
            return res * sign
