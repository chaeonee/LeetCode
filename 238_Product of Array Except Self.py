class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        answer = [1] * N
        for i in range(N-1):
            answer[i+1] = nums[i] * answer[i]

        num = 1
        for i in range(N-1, -1, -1):
            answer[i] *= num
            num *= nums[i]

        return answer
        
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p_num, n_zero = 1, 0
        for n in nums:
            if n == 0:
                n_zero += 1
            else:
                p_num *= n

        result = []
        for n in nums:
            if n == 0:
                if n_zero - 1 == 0:
                    result.append(p_num)
                else:
                    result.append(0)
            else:
                if n_zero == 0:
                    result.append(p_num//n)
                else:
                    result.append(0)

        return result
'''
