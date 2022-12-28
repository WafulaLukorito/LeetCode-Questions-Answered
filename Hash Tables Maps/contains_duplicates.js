/** 
""" Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Leetcode 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Topics: Array, Hash Table
# Complexity: Time: O(N)--- N --> Length of input array
# Difficulty: Easy

 #? Can use three methods:
 1. sort array and check if nums[i] == nums [i-1]
 2. Create set and check if set is equal to array.
 #?3. Use map to track items --- Time O(N)--- single loop over input array. Space O(N)--- We create map to track

 #Example 1: 
    Input: nums = [1,2,3,1]
    Output: true

    #Example 2:
    Input: nums = [1,2,3,4]
    Output: false
"""
*/


// var containsDuplicates = function(nums) {
//     myMap = {}
//     for (let num of nums) {
//         if (num in myMap) {
//             return true;

//         }
//         myMap[num] = true;
//     }
//     return false;
// };

//using set
function containsDuplicates(nums) {
    return new Set(nums).size !== nums.length;
}


nums1 = [1, 2, 3, 4, 1];
nums2 = [1, 2, 3, 4, 5, 6];

console.log(containsDuplicates(nums1)); // true
console.log(containsDuplicates(nums2)); // false