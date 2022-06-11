let productExceptSelf = (nums) => {
  let products = [];

  for (let num of nums) {
    let sum = nums.reduce((a, b) => a * Math.abs(b));
    sum /= num;
    products.push(sum);
  }

  return products;
};

console.log(9 / 0);
console.log(productExceptSelf([-1, 1, 0, -3, 3]));
