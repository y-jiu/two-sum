# This is a sample Python script.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      self.num_dict = {}

      for i, num in enumerate(nums):
        self.complement = target - num

        if self.complement in self.num_dict:
          return [self.num_dict[self.complement], i]

        self.num_dict[num] = i

      return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  nums = [3, 2, 4]
  target = 6
  sol = Solution()
  result = sol.twoSum(nums, target)
  print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
