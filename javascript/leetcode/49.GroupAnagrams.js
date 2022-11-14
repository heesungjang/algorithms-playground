var groupAnagrams = function (strs) {
  const map = {};

  for (const word of strs) {
    const sortedWord = [...word].sort().join('');

    if (sortedWord in map) {
      map[sortedWord].push(word);
    } else {
      map[sortedWord] = [word];
    }
  }

  return Object.entries(map).map(([key, value]) => value);
};

console.log(groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']));
