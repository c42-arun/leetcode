import sys
sys.path.insert(0, "../../src/two_sum")

try:
    from s3_hash_table_1_pass import Solution
except ImportError:
    print('No Import')

def test_answer():
    expectedAnswer = [0,1]
    sn = Solution()
    answer = sn.twoSum([3,3], 6)
    assert(len(expectedAnswer) == len(answer) and sorted(expectedAnswer) == sorted(answer))    