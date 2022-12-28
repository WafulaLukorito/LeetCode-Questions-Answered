/**Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Leetcode: https://leetcode.com/problems/majority-element/
Difficulty: Easy


#? Time Complexity: O(2*N) = O(N)---One pass to assign value, separate pass again

#?Space: O(N)--- create a map to track occurrence

#! Use m.get!!! */
var majorityElement = (nums) => {
    let numToFreq = {};
    let numslen = nums.length;
    for (let num of nums) {
        if (!(num in numToFreq)) {
            numToFreq[num] = 1;
        } else {
            numToFreq[num]++;
            if (numToFreq[num] > numslen / 2) {
                return num;
            }
        }
    }
    return -1; // Return -1 if no majority element is found
};

let nums = [2, 2, 1, 1, 1, 2, 2, 2];
let res = majorityElement(nums);
console.log(`The majority element in array ${nums} is ${res}`);


/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
        let m = new Map();
        for (let i = 0; i < nums.length; i++) {
            if (m.has(nums[i])) {
                m.set(nums[i], m.get(nums[i]) + 1)
            } else {
                m.set(nums[i], 1)
            }
            if (m.get(nums[i]) > nums.length / 2) {
                return nums[i]
            }
        }