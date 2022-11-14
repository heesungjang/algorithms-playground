var topKFrequent = function (nums, k) {
  const map = {};
  const answer = [];
  for (let num of nums) {
    if (num in map) {
      map[num] += 1;
    } else {
      map[num] = 1;
    }
  }

  for (let prop in map) {
    answer.push([prop, map[prop]]);
  }

  answer.sort((a, b) => b[1] - a[1]);
  return answer.slice(0, k).map((item) => parseInt(item[0]));
};

console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2));
