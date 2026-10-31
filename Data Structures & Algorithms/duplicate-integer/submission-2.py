class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos = set()
        for i in range(len(nums)):
            if(nums[i] in vistos):
                return True
            vistos.add(nums[i])
        return False
        