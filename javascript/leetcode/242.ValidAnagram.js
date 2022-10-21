/*
 * 정렬
 * 시간 복잡도 O(N)
 * 공간 복잡도 O(1)
 * 리드코드 런타임 시간: 112 ms (77.71%)
 */

var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;
  s = s.split('').sort().join('');
  t = t.split('').sort().join('');

  return s === t;
};

/**
 * 해쉬 맵
 * 시간복잡도:O(N)
 * 공간복잡도:O(N)
 * 리드코드 런타임 시간: 133 ms (54.60%)
 */

var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;

  const map = {};

  for (const char of s) {
    if (char in map) {
      map[char] += 1;
    } else {
      map[char] = 1;
    }
  }

  for (const char of t) {
    if (char in map) {
      map[char] -= 1;
    } else {
      map[char] = 0;
    }
  }

  for (value of Object.values(map)) {
    if (value !== 0) {
      return false;
    }
  }

  return true;
};
