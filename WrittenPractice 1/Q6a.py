"""
Error:
You are replacing the entire list with the calculated value

call the append method on the list but remove the reassignment to nums

"""

nums = [1, 2, 3, 4, 5]
nums.append(nums[0] + nums[-1])
#nums = nums.append(nums[0] + nums[-1])

print(nums)