// 정렬 (two Pointer 방식)
const targetNum = 10;
const array = [3, 5, -4, 8, 11, 1, -1, 6];
function twoNumberSumPointer(array, targetNum) {
  const sortedArray = array.sort((a, b) => a - b);

  let left = 0;
  let right = array.length - 1;

  while (left < right) {
    const currentSum = array[left] + array[right];
    if (currentSum === targetNum) {
      return [array[left], array[right]];
    } else if (currentSum < targetNum) {
      left++;
    } else if (currentSum > targetNum) {
      right--;
    }
  }
  return [];
}
console.log(twoNumberSumPointer(array, targetNum));

// 정렬 (Brute Force Approach 방식)
function twoNumberSumBrute(array, targetNum) {
  for (let i = 0; i < array.length - 1; i++) {
    const firstNum = array[i];
    for (let j = i + 1; j < array.length; j++) {
      const secondNum = array[j];
      if (firstNum + secondNum === targetNum) {
        return [firstNum, secondNum];
      }
    }
  }
  return [];
}

console.log(twoNumberSumBrute(array, targetNum));

// 정렬 (hash table 방식)
/**
 *
 * const targetNum = 10;
 * const array = [-4, -1, 1,  3, 5,  6, 8, 11]
 *  -4
 *   -1
 *   1
 *   3
 *   5
 *   6
 *   8
 *   --break
 * }
 */
function twoNumberSumHash(array, targetNum) {
  let temp = [];

  for (const currentNum of array) {
    let potentialMatch = targetNum - currentNum;
    if (potentialMatch in temp) {
      return [potentialMatch, currentNum];
    } else {
      temp[currentNum] = true;
    }
  }

  return [];
}

console.log(twoNumberSumHash(array, targetNum));
