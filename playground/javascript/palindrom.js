const target = "A man, a plan, a canal: Panama";

function isPalindrome(string) {
  const isAlnum = /^[a-zA-Z0-9]*$/;

  let arr = [];
  for (i = 0; i < string.length; i++) {
    if (isAlnum.test(string[i])) {
      arr.push(string[i].toLowerCase());
    }
  }
  const targetStrings = arr.join("");

  let leftIndex = 0;
  let rightIndex = targetStrings.length - 1;

  while (leftIndex < rightIndex) {
    if (targetStrings[leftIndex] !== targetStrings[rightIndex]) {
      return false;
    }
    leftIndex++;
    rightIndex--;
  }
  return true;
}

console.log(isPalindrome(target));
