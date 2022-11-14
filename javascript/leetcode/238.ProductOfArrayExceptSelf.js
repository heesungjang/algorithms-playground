var productExceptSelf = function (nums) {
  const answer = [];

  nums.reduce((prev, acc, i) => {
    answer[i] = prev;
    return prev * acc;
  }, 1);

  nums.reduceRight((prev, acc, i) => {
    answer[i] *= prev;
    return prev * acc;
  }, 1);

  return answer;
};

console.log(productExceptSelf([1, 2, 3, 4]));
console.log(productExceptSelf([-1, 1, 0, -3, 3]));
