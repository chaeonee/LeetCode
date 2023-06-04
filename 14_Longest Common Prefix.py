class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for string in strs[1:]:
            if not prefix:
                break

            idx = 0
            while idx < len(string) and idx < len(prefix):
                if string[idx] != prefix[idx]:
                    break
                idx += 1
                      
            prefix = prefix[:idx]

        return prefix
