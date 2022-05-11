/*
From Free Code Camp DP course, https://www.youtube.com/watch?v=oBt53YbR9Kk&t=194s
*/

//*Fibonacci Problem

//Recursive method, time compexity //*O(2^n) time
//Space //*O(n)

// const fib = (n) => {
//     if (n <= 2) return 1;
//     return fib(n - 1) + fib(n - 2);
// };

//* Memoisation --?
//* js object, keys will be arguments to fn, value will be return value
//todo Time Complexity --> O(n), linear
//*Space complexity --> O(n)

const fib = (n, memo = {}) => {
    if (n in memo) return memo[n];
    if (n <= 2) return 1;
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
    return memo[n]
};



// console.log(fib(6));
// console.log(fib(7));
// console.log(fib(8));
// console.log(fib(60));


//! GRTID TRAVELLER

/*
Say you are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner.
You may only move down and right.
In how many ways can you travel to the goal on a grid with dimensions m * n?
*/

//*recursive Brute Force
//Time --> O(2^(n+m))
//Space --> O(n+m)
//! bad!
// const gridTraveller = (m, n) => {
//     if (m === 1 && n == 1) return 1
//     if (m === 0 || n == 0) return 0
//     return (gridTraveller(m - 1, n) + (m, n - 1))

// };

//*Memoisation

//Time Coplexity ==>O(m*n)
//Space Complexity ==> O(n+m)

const gridTraveller = (m, n, memo = {}) => {
    //Create unque identifier by transforming into string
    const key = m + ',' + n;
    //Are the arguments in the memo?
    if (key in memo) return memo[key];
    if (m === 1 && n == 1) return 1;
    if (m === 0 || n == 0) return 0;

    memo[key] = gridTraveller(m - 1, n, memo) + gridTraveller(m, n - 1, memo);
    return memo[key];

};

// console.log(gridTraveller(1, 1));
// console.log(gridTraveller(2, 3));
// console.log(gridTraveller(3, 2));
// console.log(gridTraveller(3, 3));
// console.log(gridTraveller(18, 18));
// console.log(gridTraveller(18, 50));
// console.log(gridTraveller(100, 100));

/*
//! ALVIN's MEMOIZATION RECIPE

1. Make it work --- could be brutefore recurcive, you'll refine later:
    - Visualize the problem as a tree
    -Implement tree using recursion
    -test it.. correct answers, though only for small values

2. Make it efficient --  Do not start with efficiency
    - *you may need to create unique identifier
    - add a memo object, mostly a default empty object
    -Add base case to return memo values 
    -store return vaues in memo

*/

//!CANSUM MEMOIZATION

/*
Write a function `canSum{targetSum, numbers}` that takes in a targetSum and an array of numbers as arguments. 
The function should return true if there is a subset of the numbers in the array that sums to the targetSum.
You may use an element of an array as many times as needed.
You may assume that all input numbers are nonnegative
*/

//*Github Co-Pilot implementation
// function canSum(targetSum, numbers) {
//     //Create a memo object
//     const memo = {};
//     //Create a function that will be called recursively
//     const canSumRecursive = (targetSum, numbers) => {
//             //Create a unique identifier
//             const key = targetSum + ',' + numbers.join(',');
//             //Is the key in the memo?
//             if (key in memo) return memo[key];
//             //If the targetSum is 0, return true
//             if (targetSum === 0) return true;
//             //If the targetSum is less than 0, return false
//             if (targetSum < 0) return false;
//             //If there are no numbers left, return false
//             if (numbers.length === 0) return false;
//             //If the first number is greater than the targetSum, remove it and call the function again
//             if (numbers[0] > targetSum) {
//                 return canSumRecursive(targetSum, numbers.slice(1));
//             }
//             //If the first number is less than or equal to the targetSum, remove it and call the function again
//             if (numbers[0] <= targetSum) {
//                 return canSumRecursive(targetSum - numbers[0], numbers.slice(1)) || canSumRecursive(targetSum, numbers.slice(1));
//             }
//         }
//         //Call the function
//     return canSumRecursive(targetSum, numbers);
// }


// console.log(canSum(0, [2, 3, 6, 7]));
// // console.log(canSum(1, [1]));
// // console.log(canSum(2, [1, 2]));
// // console.log(canSum(3, [1, 2, 3]));
// // console.log(canSum(4, [1, 2, 3]));
// // console.log(canSum(5, [1, 2, 3]));
// // console.log(canSum(6, [1, 2, 3]));

//* Time Complexity --> O(n^m) --> exponential time  (m (target sum) levels multiplied by itself n times (array length) levels)
//* Space Complexity --> O(m) --> linear space (height os the tree is m)

const canSumRecursive = (targetSum, nums) => { //O(n^2)
    if (targetSum === 0) return true;
    if (targetSum < 0) return false;

    for (let num of nums) {
        const remainder = targetSum - num;
        if (canSumRecursive(remainder, nums) === true) {
            return true;
        }
    }
    return false;
};


// console.log(canSumRecursive(4, [9, 3, 6, 7]));
// console.log(canSumRecursive(5, [9, 3, 6, 7]));
// console.log(canSumRecursive(6, [9, 3, 6, 7]));
// console.log(canSumRecursive(300, [7, 14]));

//*Memoization
//* O(m*n) time complexity
//* O(m) space complexity

const canSumMemo = (targetSum, nums, memo = {}) => {
    if (targetSum in memo) return memo[targetSum];
    if (targetSum === 0) return true;
    if (targetSum < 0) return false;

    for (let num of nums) {
        const remainder = targetSum - num;
        if (canSumMemo(remainder, nums, memo) === true) {
            memo[targetSum] = true;
            return true;
        }
    }
    memo[targetSum] = false;
    return false;
};



console.log(canSumMemo(0, [2, 3, 6, 7]));
console.log(canSumMemo(1, [1]));

console.log(canSumMemo(4, [9, 3, 6, 7]));
console.log(canSumMemo(5, [9, 3, 6, 7]));
console.log(canSumMemo(6, [9, 3, 6, 7]));
console.log(canSumMemo(300, [7, 14]));
console.log(canSumMemo(2, [1, 2]));
console.log(canSumMemo(3, [1, 2, 3]));
console.log(canSumMemo(4, [1, 2, 3]));
console.log(canSumMemo(5, [1, 2, 3]));
console.log(canSumMemo(6, [1, 2, 3]));


//!HOWSUM PROBLEM

/*
Write a function `howSum(int targetSum, int[] numbers)` that takes in a 
target sum and an array of numbers as arguments.
 
The function should return an array containing any combination of
elements that add up to exactly the target sum. If there is no
combination that adds up to the target sum, then return null.
 
If there are multiple combinations possible, you may return any
single one.
*/


