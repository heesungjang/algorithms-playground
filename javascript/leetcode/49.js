const strs = ["eat", "tea", "tan", "ate", "nat", "bat"];

var groupAnagrams = function (strs) {
  const obj = {};
  for (let str of strs) {
    const sorted_str = str.split("").sort().join("");
    if (sorted_str in obj) {
      obj[sorted_str].push(str);
    } else {
      obj[sorted_str] = [str];
    }
  }

  const answer = [];
  for (const [key, value] of Object.entries(obj)) {
    answer.push(value);
  }

  return answer;
};

groupAnagrams(strs);
