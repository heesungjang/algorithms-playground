s = "anagram";
t = "nagaram";

let isAnagram = function (s, t) {
  if (s.length !== t.length) {
    return false;
  }
  sObj = {};
  tObj = {};

  for (let char of s) {
    if (char in sObj) {
      sObj[char] += 1;
    } else {
      sObj[char] = 1;
    }
  }

  for (let char of t) {
    if (char in tObj) {
      tObj[char] += 1;
    } else {
      tObj[char] = 1;
    }
  }

  for (let char of s) {
    if (sObj[char] !== tObj[char]) {
      return false;
    }
  }

  return true;
};

console.log(isAnagram(s, t));

/**
 * 송현님: 너무 못한다고 생각한다.
 * 하는데, 막상 하려고 하면 어렵다.
 * 리덕스 전에는 좀 했는데, 지금은 정말 모르겠다.
 *
 * 카운터를 만드는데, 오류가 생기면 --> 어디서 발생했는지 모르겠다.
 *
 * 종훈님: 솔직히 툴킷부터, 리덕스 까지는 괜찮다.
 * 리듀서가 state랑 action을 사용하는데, filter--> id를 사용하는데 --> state.payload
 *
 *
 * 민희님: 흐름은 알겠는데, 개념이 리셋한다 --> check box --> 모달? -->
 *
 * 중희님:
 */
