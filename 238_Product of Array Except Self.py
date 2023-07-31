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
