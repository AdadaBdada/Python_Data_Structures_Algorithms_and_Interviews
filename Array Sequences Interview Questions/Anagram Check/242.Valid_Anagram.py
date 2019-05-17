"""https://leetcode.com/problems/valid-anagram/"""

Class Solution(object):
    def isAnagram(slef, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s = s.replace(" ","").lower()
        t = t.replace(" ","").lower()
        # Edge Case to check if same nunmber of letters

        if len(s) != len(t):
            return False

        count={}
        for letter in s:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1

        for letter in t:
            if letter in count:
                count[letter] -= 1
            else:
                count[letter] = 1

        for k in count:
            if count[k] != 0:
                return False

        return True
