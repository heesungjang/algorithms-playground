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
