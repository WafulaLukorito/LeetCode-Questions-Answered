/** 
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Leetcode: https://leetcode.com/problems/4sum-ii/
Leetcode Number: 454
Difficulty: Medium
Category: Hash Tables Maps
"""

# ? Time Complexity: O(N^2)--- N is the maximum size of the 4 input arrays. We do a nested loop twice.

# ?Space Complexity: O(N)-- Due to usage of maps

# ? Approach: We can use a map to store the sum of the first two arrays. Then we can iterate through the last two arrays and check if the sum of the last two arrays is equal to the negative of the sum of the first two arrays. If it is, we can increment the answer by the number of times the sum of the first two arrays occurs.
*/

// var fourSumCount = function(nums1, nums2, nums3, nums4) {
//     let map = new Map();
//     let ans = 0;
//     for (let i = 0; i < nums1.length; i++) {
//         for (let j = 0; j < nums2.length; j++) {
//             let sum = nums1[i] + nums2[j];
//             map.set(sum, map.get(sum) + 1 || 1);
//         }
//     }
//     for (let i = 0; i < nums3.length; i++) {
//         for (let j = 0; j < nums4.length; j++) {
//             let sum = nums3[i] + nums4[j];
//             if (map.has(-sum)) {
//                 ans += map.get(-sum);
//             }
//         }
//     }
//     return ans;
// };

var fourSumCount = function(nums1, nums2, nums3, nums4) {
    let sumMap = {};
    let res = 0;

    for (let i = 0; i < nums1.length; i++) {
        for (let j = 0; j < nums2.length; j++) {
            let mySum = nums1[i] + nums2[j];
            if (mySum in sumMap) {
                sumMap[mySum]++;

            }
            sumMap[mySum] = 1;
        }
    }
    for (let i = 0; i < nums3.length; i++) {
        for (let j = 0; j < nums4.length; j++) {
            let goal = -(nums3[i] + nums4[j]);
            if (goal in sumMap) {
                res += sumMap[goal];
            }
        }
    }
    return res;
};

// ? Test Cases:
console.log(fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2])); // 2
console.log(fourSumCount([0], [0], [0], [0])); // 1