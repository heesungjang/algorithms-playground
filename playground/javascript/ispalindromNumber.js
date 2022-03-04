const x = -121;

var isPalindrome = function (x) {
  let stringX = x.toString();
  let leftIdx = 0;
  let rightIdx = stringX.length - 1;

  while (leftIdx < rightIdx) {
    if (stringX[leftIdx] === stringX[rightIdx]) {
      leftIdx++;
      rightIdx--;
    } else {
      return false;
    }
  }
  return true;
};

console.log(isPalindrome(x));
