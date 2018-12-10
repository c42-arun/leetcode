class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i in range(len(nums)):
            # does the complement exist as a key in the hash table (and is not the same as the number itself)
            complement = target - nums[i]
            if complement in num_dict and num_dict[complement] != i:
                return [i, num_dict[complement]]
                
            # number is the key; its index is the value in the Hash table
            num_dict[nums[i]] = i                

        return []


if __name__ == '__main__':
    sn = Solution()
    answer = sn.twoSum([3,3], 6)
    print(answer)

def test_answer():
    expectedAnswer = [0,1]
    sn = Solution()
    answer = sn.twoSum([3,3], 6)
    assert(len(expectedAnswer) == len(answer) and sorted(expectedAnswer) == sorted(answer))