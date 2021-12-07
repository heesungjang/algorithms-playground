// is sequence given subsequence of array?
//output: boolean

const array = [5, 1, 22, 25, 6, -1, 8, 10];
const sequence = [1, 6, -1, 10];

function validateSubsequence(array, sequence) {
  let targetIdx = 0;

  for (let num of array) {
    if (targetIdx === sequence.length) break;
    if (num === sequence[targetIdx]) targetIdx++;
  }
  return targetIdx === sequence.length;
}

console.log(validateSubsequence(array, sequence));
