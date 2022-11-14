/**
 * 브루트포스
 */

var twoSome = function (nums, target) {
  let answer;

  for (i = 0; i < nums.length - 1; i++) {
    for (j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        answer = [i, j];
      }
    }
  }

  return answer;
};

comments.push(res.data);
/**
 * 해쉬
 */

var twoSome = function (nums, target) {
  const hash = new Map();

  for (i = 0; i < nums.length; i++) {
    const pair = target - nums[i];
    if (hash.has(pair)) {
      return [i, hash.get(pair)];
    } else {
      hash.set(nums[i], i);
    }
  }
};
