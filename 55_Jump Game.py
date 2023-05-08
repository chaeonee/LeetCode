class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        
        max_jump = 0
        for i, n in enumerate(nums):
            if max_jump < i:
                break

            max_jump = max(max_jump, i + n)
            
            if max_jump >= N-1:
                return True
        
        return False
