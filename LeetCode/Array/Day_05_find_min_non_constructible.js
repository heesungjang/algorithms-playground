/**
 * find the min min_non_constructible
 * expected output = 20
 *
 */

const coins = [5, 7, 1, 1, 2, 3, 22];

function getMinNonConstructible(coins) {
  // 코인 정렬
  coins.sort((a, b) => a - b);

  let minValueCandidate = 1;

  // [1,1,2,3,5,7,22]
  // 1 >  1?  x = 2
  // 1 >  2? x = 3
  // 2 > 3? x = 5
  // 3 > 5? x = 8
  // 5 > 8? x = 13
  // 7 > 13? x = 20
  // 22 > 20? o = return 20
  for (let i = 0; i < coins.length; i++) {
    if (coins[i] > minValueCandidate) return minValueCandidate;
    else minValueCandidate = coins[i] + minValueCandidate;
  }

  return minValueCandidate;
}

console.log(getMinNonConstructible(coins));
