class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_num = len(nums)
        for s in range(n_num):
            for e in range(s+1, n_num):
                if nums[s] + nums[e] == target:
                    return [s,e]
