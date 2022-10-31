class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, j in enumerate(nums):
            if (target-j) in dictionary.keys():
                return [dictionary[target-j], i]
            else:
                dictionary[j] = i