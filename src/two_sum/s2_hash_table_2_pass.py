class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i in range(len(nums)):
            num_dict[nums[i]] = i #  number is the key; its index is the value in the Hash table

        for i in range(len(nums)):
            complement = target - nums[i]

            # does the complement exist as a key in the hash table (and is not the same as the number itself)
            if complement in num_dict and num_dict[complement] != i:
                return [i, num_dict[complement]]

        return []


if __name__ == '__main__':
    sn = Solution()
    answer = sn.twoSum([2, 7, 11, 15], 9)
    print(answer)
