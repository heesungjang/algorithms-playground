// 정렬 (two Pointer 방식)
const targetNum = 10;
const array = [3, 5, -4, 8, 11, 1, -1, 6];
function twoNumberSum(array, targetNum) {
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

console.log(twoNumberSum(array, targetNum));
