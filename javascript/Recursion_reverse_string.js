// 재귀함수 문자열 뒤집기

let result = "";
let TARGET_STRING = "jangheesung";

// 문자열 뒤에 result를 넣으면 정순으로 출력한다.1
// while (true) {
//     if (TARGET_STRING.length == 1) {
//         result = TARGET_STRING + result;
//         break;
//     }

//     let TARGET_ARRAY = TARGET_STRING.split("");
//     result = String(TARGET_ARRAY.pop()) + result;
//     TARGET_STRING = TARGET_ARRAY.join("");
// }

while (true) {
    if (TARGET_STRING.length == 1) {
        result += TARGET_STRING;
        break;
    }

    let targetArray = TARGET_STRING.split("");
    result += targetArray.pop();
    TARGET_STRING = targetArray.join("");
}

console.log(result);

function 문자열뒤집기(문자) {
    if (문자.length == 1) {
        return 문자;
    }

    return 문자[문자.length - 1] + 문자열뒤집기(문자.slice(0, 문자.length - 1));
}

console.log(문자열뒤집기("jangheesung"));
// 순번     return
//  1       문자열뒤집기(문자.slice(0, 문자.length - 1)) + 문자[문자.length - 1];
//  2
//  3
//  4
//  5
