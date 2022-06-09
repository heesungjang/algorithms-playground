const nums = [1, 1, 1, 2, 2, 3];
const k = 2;

let topFrequent = function (nums, k) {
  let map = {};
  const answer = [];

  // counting
  for (let num of nums) {
    if (num in map) {
      map[num] += 1;
    } else {
      map[num] = 1;
    }
  }

  let sortedMap = Object.entries(map)
    .sort(([, a], [, b]) => a - b)
    .reverse()
    .slice(0, k);

  //   console.log(sortedMap);
  for (let item of sortedMap) {
    answer.push(parseInt(item[0]));
  }
  return answer;
};
