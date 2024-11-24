def find_two_sum(nums, target):
    seen = {}  # Dictionary to store seen numbers
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]  # Return indices
        seen[num] = i
    return None  # If no pair is found

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = find_two_sum(nums, target)
print(result)  # Output: [0, 1]
