// 재귀 함수 합
function f(n) {
    // 종료 조건 --> 만약 없다면 무한 반복이 실행된다.
    if (n <= 1) {
        return 1;
    }

    return n + f(n - 1);
}

// 재귀 함수 곱
function x(n) {
    if (n <= 1) {
        return x;
    }

    return n * f(n - 1);
}
console.log("재귀함수:", f(100));
console.log("재귀함수:", x(100));
