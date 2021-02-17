/**
 * Version natural de factorial.
 */
const factorial = (n) => {
  if (n < 1) return 1;
  return n * factorial(n - 1);
};

/**
 * Version de cola de factorial.
 */
const factorialTail = (n) => {
  let helper = (i, acc) => {
    if (i < 1) return acc;
    return helper(i - 1, acc * i);
  };

  return helper(n, 1);
};
