#!/usr/bin/python3
class Solution:
    def twoSum(self, nums, target):
        tempnums = nums[:]
        success = False
        while len(tempnums) > 1:
            if success : break
            first = tempnums.pop(0)
            for num in tempnums:
                if first + num == target:
                    second = num
                    success = True
                    break
        idx1 = nums.index(first)
        idx2 = nums.index(second,idx1+1)
        return [idx1, idx2]
