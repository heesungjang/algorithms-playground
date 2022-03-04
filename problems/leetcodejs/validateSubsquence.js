const array = [5, 1, 22, 25, 6, -1, 8, 10];
const sequence = [1, -1, 6, 10];
function isValidSubsequence(array, sequence) {
  let arrayIdx = 0;
  let sequenceIdx = 0;

  while (arrayIdx < array.length && sequenceIdx < sequence.length) {
    if (array[arrayIdx] === sequence[sequenceIdx]) {
      sequenceIdx++;
    }
    arrayIdx++;
  }
  return sequence.length === sequenceIdx;
}

console.log(isValidSubsequence(array, sequence));
