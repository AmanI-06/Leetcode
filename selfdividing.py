
def is_self_dividing(x):
    s = str(x)
    for d in s:
        if d=="0" or x%int(d)!=0:
            return False
    return True

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for x in xrange(left, right+1):
            if is_self_dividing(x):
                ans.append(x)
        return ans