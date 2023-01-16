//Check if a number is odd

function isOdd(num) {
    if (num % 2 === 1) {
        console.log("Yes, the number is odd");
    } else {
        console.log("No, the number is not odd")
    }
}

myNum = 55;
myNum2 = 56;

isOdd(2);
//isOdd(myNum2);

/**
 * Write a function called count_odd_numbers that takes in a list of integers and returns the count of odd numbers in the list. For example:

Copy code
count_odd_numbers([1, 2, 3, 4, 5])  # 3
count_odd_numbers([10, 12, 14, 16]) # 0
count_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # 5
 */

// function count_odd_numbers(nums) {
//     let count = 0;
//     for (let i = 0; i < nums.length; i++) {
//         if (nums[i] % 2 === 1) {
//             count++;
//         }
//     }
//     return count;
// }

// console.log(count_odd_numbers([10, 12, 14, 16]));

// console.log(count_odd_numbers([1, 2, 3, 4, 5]));

// console.log(count_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));