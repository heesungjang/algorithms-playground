/**
 * Hash Set 사용
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N)
 * 리드코드 런타임 시간: 151 ms
 */

var containsDuplicate = function (nums) {
  const numsSet = new Set([...nums]);
  return numsSet.size !== nums.length;
};

/**
 * Hash map - early exit
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N)
 * 리드코드 런타임 시간: 92 ms
 */

var containsDuplicate = function (nums) {
  numsSet = {};

  for (const num of nums) {
    if (num in numsSet) {
      return true;
    }
    numsSet[num] = 0;
  }

  return false;
};

console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]));

/**
 * 정렬
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N)
 * 리드코드 런타임 시간: 157 ms
 */
var containsDuplicate = function (nums) {
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[i] === nums[i + 1]) {
      return true;
    }
  }
  return false;
};
