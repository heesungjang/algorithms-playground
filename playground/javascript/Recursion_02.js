// 재귀 함수 합
function f(n) {
    // 종료 조건 --> 만약 없다면 무한 반복이 실행된다.
    if (n <= 1) {
        return 1;
    }

    return n + f(n - 1);
}

// 재귀 함수 곱

//      순번         x(n)       n       return              최종
//      1             x(5)       5      5 * x(5-1)         5* 24 == 120
//      2            x(4)       4      4 * x(4-1)         4* 6 == 24
//      3            x(3)       3      3 * x(3-1)         3* 2 == 6
//      4           x(2)        2      2 * x(2-1)         2* 1 == 2
//      5           x(1)        1       1                       1

function x(n) {
    if (n <= 1) {
        return 1;
    }

    return n * x(n - 1);
}
console.log("재귀함수:", f(100));
console.log("재귀함수:", x(5));
