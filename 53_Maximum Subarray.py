class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_sum, max_sum = 0, nums[0]
        for num in nums:
            if sub_sum < 0:
                sub_sum = 0
            sub_sum += num

            max_sum = max(sub_sum, max_sum)

        return max_sum
