/**
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

LeetCode: https://leetcode.com/problems/two-sum/
LeetCode Number: 1
Difficulty: Easy
Topic: Hash Tables, Maps
Company: Amazon, Apple, Facebook, Google, Microsoft, Uber, Yahoo

#? Time O(N): We do a loop over array of size n
#? Space O(N): We create a map to hold a value alongside the index
*/

// function twoSum(nums, target) {
//     let map = new Map();
//     for (let i = 0; i < nums.length; i++) {
//         let complement = target - nums[i];
//         if (map.has(complement)) {
//             return [map.get(complement), i];
//         }
//         map.set(nums[i], i);
//     }
//     return null;
// }

var twoSum = function(nums, target) {
    let numToIndex = {};
    for (let i = 0; i < nums.length; i++) {
        let goal = target - nums[i];
        if (goal in numToIndex) {
            return [i, numToIndex[goal]];
        }
        numToIndex[nums[i]] = i;
    }
    return null;
};

var nums = [3, 3];
var target = 6;

var result = twoSum(nums, target);

console.log(twoSum([2, 7, 11, 15], 9)); // [0, 1]
console.log(twoSum([3, 2, 4], 6)); // [1, 2]
console.log(twoSum([3, 3], 6)); // [0, 1]
console.log(twoSum([3, 2, 3], 20)); // null

var twoSum2 = function(nums, target) {
    numToIndex = {};
    for (let i = 0; i < nums.length; i++) {
        let goal = target - nums[i];
        if (goal in numToIndex) {
            return ([i, numToIndex[goal]]);
        }
        numToIndex[nums[i]] = i;
    }
    return null;
};

var nums = [3, 4, 5];
var target = 8;

var result = twoSum2(nums, target);

console.log(result);