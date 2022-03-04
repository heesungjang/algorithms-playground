// 재귀함수
// 내가 나를 호출하는 함수
// 반복문 <-> 재귀함수
// 재귀 함수는 반복문과 호환이 가능하다.

let s = 0;

for (var i = 1; i < 101; i++) {
    s += i;
}

let m = 1;

for (var i = 1; i < 6; i++) {
    m *= i;
}

let n = 100;

console.log((n * (n + 1)) / 2);

console.log(s);
// O(n)

console.log(n);
// O(1)
