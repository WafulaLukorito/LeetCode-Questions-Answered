class Solution:
    def solution(self, nums, ans, cur, index):
        """
        Recursive helper function to generate subsets using backtracking.

        Args:
            nums (list): The input list of numbers.
            ans (list of lists): The list to store the generated subsets.
            cur (list): The current subset being built.
            index (int): The starting index in 'nums' to consider for adding elements to 'cur'.
        """
        # Base case: When the index goes beyond the length of 'nums',
        # it means we have considered all possible elements.
        # At this point, the 'cur' list represents a complete subset,
        # so we add a copy of it to our 'ans' list.
        if index > len(nums):
            return

        # Add the current subset ('cur') to the list of all subsets ('ans').
        # We append a copy of 'cur' using slicing [:] to avoid modifying
        # the 'ans' list when 'cur' is updated later.
        ans.append(cur[:])

        # Iterate through the remaining elements in 'nums' starting from the current 'index'.
        for i in range(index, len(nums)):
            # Optimization: Only add the current number if it's not already in the current subset ('cur').
            # This prevents duplicate numbers within a single subset, although the problem statement
            # doesn't explicitly mention unique numbers in the input. If duplicates are allowed
            # in the input and should be considered in subsets, this condition should be removed.
            if nums[i] not in cur:
                # Include the current number (nums[i]) in the current subset ('cur').
                cur.append(nums[i])

                # Recursively call the 'solution' function to explore further subsets
                # starting from the next index (i+1). By starting from i+1, we ensure
                # that we don't consider the same element again in the current branch
                # of the recursion, which helps in generating distinct subsets (without repetition
                # of elements in the order they appear in 'nums').
                self.solution(nums, ans, cur, i + 1)

                # Backtrack: After the recursive call returns, we need to remove the last
                # added element from 'cur'. This is crucial for exploring other possibilities.
                # By popping the last element, we effectively undo the choice we made
                # in the current iteration of the loop and allow the loop to consider
                # the next element for inclusion in the subset.

                cur.pop()

    def subsets(self, nums):
        """
        Generates all possible subsets of a given list of numbers.

        Args:
            nums (list): The input list of numbers.

        Returns:
            list of lists: A list containing all possible subsets of 'nums'.
        """
        # Initialize an empty list to store the current subset being built during recursion.
        cur = []
        # Initialize an empty list to store the final result, which will contain all subsets.
        ans = []
        # Call the recursive helper function 'solution' to generate the subsets.
        # We start the process with an empty current subset ('cur') and from the beginning of the 'nums' list (index 0).
        self.solution(nums, ans, cur, 0)
        # Return the list containing all generated subsets.
        return ans

# Test case
nums = [1, 2, 3]
expected_output = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

# Create an instance of the Solution class
sol = Solution()
# Call the 'subsets' method on the instance to get the result.
output = sol.subsets(nums)

# Sorting both lists of lists to ensure order doesn't matter for comparison
output_sorted = sorted([sorted(sublist) for sublist in output])
expected_output_sorted = sorted([sorted(sublist) for sublist in expected_output])

if output_sorted == expected_output_sorted:
    print ("Test Passed!", output)
else:
    print ("Test Failed!")
    print ("Output:", output)
    print ("Expected:", expected_output)