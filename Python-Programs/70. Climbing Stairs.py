class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 2):
            return 2
        if(n == 1):
            return 1
        return self.climbStairs(n-1)+self.climbStairs(n-2)