class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}
        for i, num in enumerate(nums):
            complemento = target - nums[i]
            if complemento in vistos:
                return [vistos[complemento], i]
            vistos[num] = i; 
        