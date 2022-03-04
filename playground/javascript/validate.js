const s = "((}}}";
var isValid = function (s) {
  const opener = "([{";
  const pair = {
    "(": ")",
    "[": "]",
    "{": "}",
  };

  let stack = [];

  for (const char of s) {
    if (opener.includes(char)) {
      stack.push(char);
    } else {
      let stackTop = stack.pop();
      if (char !== pair[stackTop]) {
        return false;
      }
    }
  }
  return stack.length < 1;
};

console.log(isValid(s));
