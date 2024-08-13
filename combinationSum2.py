from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, end, target, path):
            if target == 0:
                res.append(path)
                return
            for i in range(start, end):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                backtrack(i + 1, end, target - candidates[i], path + [candidates[i]])
        
        candidates.sort()
        res = []
        backtrack(0, len(candidates), target, [])
        return res
