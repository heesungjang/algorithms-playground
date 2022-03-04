const paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.";

const banned = ["hit"];

function mostCommonWord(paragraph, banned) {
  const bannedSet = new Set(banned); // 중복 제거

  const words = paragraph.toLowerCase().split(/\W+/);

  let map = {};
  for (const word of words) {
    if (!bannedSet.has(word)) {
      if (map[word] == null) {
        map[word] = 1;
      } else {
        map[word]++;
      }
    }
  }

  let mostCommon;
  let maxCount = -Infinity;

  for (const word in map) {
    const count = map[word];
    if (count > maxCount) {
      mostCommon = word;
      maxCount = count;
    }
  }

  return mostCommon;
}

console.log(mostCommonWord(paragraph, banned));
