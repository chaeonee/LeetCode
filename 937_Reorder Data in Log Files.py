class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let = []
        dig = []
        for log in logs:
            log = log.split()
            if ''.join(log[1:]).isdigit():
                dig.append(' '.join(log))
            else:
                let.append(log)

        let = [' '.join(l) for l in sorted(let, key=lambda x:[x[1:], x[0]])]
        
        return let + dig
