/**
 * Calcula el producto de dos matrices.
 */
const product = (A, B) => {
  let preconditions = (A, B) =>
    isValidMatrix(A) && isValidMatrix(B) && canMultiply(A, B);

  if (!preconditions(A, B))
    throw new Error('A y B deben ser matrices validas para el producto');

  let Bt = transpose(B);
  return A.map((a) => Bt.map((b) => sumArray(a.map((_, i) => a[i] * b[i]))));
};

/**
 * Predicado que retorna si una fila de una matriz es valida.
 */
const isValidRow = (A, R) => A.includes(R) && R.length === A[0].length;

/**
 * Predicado que retorna si una matriz es valida.
 */
const isValidMatrix = (A) =>
  Array.isArray(A) &&
  !!A.length &&
  A.reduce((acc, r) => isValidRow(A, r) && acc, true);

/**
 * Predicado que retorna si dos matrices son multiplicables.
 */
const canMultiply = (A, B) => A[0].length === B.length;

/**
 * Calcula la transpuesta de una matriz.
 */
const transpose = (A) => {
  if (!isValidMatrix(A)) throw new Error('La matriz debe ser valida');

  let At = A[0].map((_) => []);

  for (let row of A) {
    for (let [j, e] of row.entries()) {
      At[j].push(e);
    }
  }

  return At;
};

/**
 * Suma los elementos de un Array.
 */
const sumArray = (A) => A.reduce((a, b) => a + b, 0);

// -------------- Corrida de ejemplo

// 5 x 4
const A = [
  [1, 2, 3, 1],
  [4, 5, 6, 1],
  [7, 8, 9, 1],
  [1, 1, 1, 1],
  [5, 7, 2, 6]
];

// 4 x 6
const B = [
  [1, 4, 7, 3, 4, 6],
  [2, 5, 8, 7, 3, 2],
  [3, 6, 9, 6, 7, 8],
  [1, 1, 1, 2, 3, 6]
];

try {
  console.log(product(A, B));
} catch (e) {
  console.log(e);
}
