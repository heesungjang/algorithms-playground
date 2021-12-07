/**
 * square and sort
 * square all element in array and sort them in same order,
 * in this case in ascending order
 *  */

// output = [1 ,4, 9, 25, 36, 64, 81]

const array = [-3, -2, 1, 4, 5, 6, 8, 9];

function squareSort(array) {
  const output = array.map((number, idx) => (array[idx] = number * number)).sort((a, b) => a - b);
  return output;
}

console.log(squareSort(array));
