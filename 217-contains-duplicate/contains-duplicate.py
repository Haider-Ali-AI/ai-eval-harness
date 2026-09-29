class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        reg = set()
        for i in range (len(nums)) :
            if nums[i] in reg:
                return True
            reg.add(nums[i])
        return False
