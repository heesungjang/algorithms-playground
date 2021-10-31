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

// 재귀함수 버전

function y(n) {
    if (n == 1 || n == 0) {
        return String(n);
    }

    return String(n % 2) + y(Math.floor(n / 2));
}

//                 Return
// y(11)        String(11 % 2) + y(Math.floor(11 / 2))  ===> 1 + 101    ===> 1101
// y(5)         String(5 %  2) + y(Math.floor(5  /  2))  ===> String(1) + 01
//y(2)          String(2 % 2) + y(Math.floor(2   /  2 )) ===> String(0) + 1 ==> 01
//y(1)            1

// reverse
function r(n) {
    if (n == 1 || n == 0) {
        return String(n);
    }
    return r(Math.floor(n / 2)) + String(n % 2);
}

//                 Return
// y(11)        r(Math.floor(11 / 2)) + String(11 % 2)  ===> 101 + String(1) ===> 1011
//y(5)          r(Math.floor(5  /  2)) + String(5 % 2)  ===> 10 + String(1)
//y(2)          r(Math.floor(2  /  2)) + String(2 % 2)  ===> 1 + String(0)
//y(1)          1

console.log(y(11));
console.log(r(11));
