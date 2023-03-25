class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        n_num = len(nums)
        nums = sorted(nums)
        for i in range(n_num-2):
            if nums[i] > 0:
                break
            left, right = i+1, n_num-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.add(tuple([nums[i], nums[left], nums[right]]))
                    right -= 1
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return result
