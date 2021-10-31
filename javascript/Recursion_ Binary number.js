// 재귀함수 2진수 변환

// target number 11 --> 2진수 표기

// 2        11      1
// 2        5       1
// 2        2       0
//           1

let result = "";
let x = 11;
while (true) {
    if (x % 2 == 0) {
        result += "0";
    } else {
        result += "1";
    }

    x = Math.floor(x / 2);

    // Math.ceil() : 소수점 올림
    // Math.floor() : 소수점 버림
    // Math.round() : 소수점 반올림

    if (x == 1 || x == 0) {
        result += String(x);
        break;
    }
}

console.log(result.split("").reverse().join(""));
