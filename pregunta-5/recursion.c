
#include <stdio.h>
#include <time.h>

typedef unsigned long int type_n;

/**
 * ---- Datos:
 * Carnet = 17-10490
 * X = 4
 * Y = 9
 * Z = 0
 * 
 * alpha = 6
 * betha = 7
 * 
 * */

// ---- Parte a)

type_n F67(type_n n)
{
    if (n < 42)
    {
        return n;
    }

    return F67(n - 7) + F67(n - 14) + F67(n - 21) + F67(n - 28) + F67(n - 35) + F67(n - 42);
}

// ---- Parte b)

type_n F67TailHelper(type_n n, type_n i, type_n t7, type_n t14, type_n t21, type_n t28, type_n t35, type_n t42)
{
    // A: Caso base: n < 42
    if (n < 42)
    {
        return n;
    }

    // B: Caso base: Ya se calculo F67(n)
    if (i < ((n % 7) + 42))
    {
        return t7;
    }

    // C: Calculo de F67(i)
    type_n f = t7 + t14 + t21 + t28 + t35 + t42;

    // D: Cambio de estado
    return F67TailHelper(n, i - 7, f, t7, t14, t21, t28, t35);
}

type_n F67Tail(type_n n)
{
    // F: Valores iniciales
    type_n m = n % 7;
    return F67TailHelper(n, n, 35 + m, 28 + m, 21 + m, 14 + m, 7 + m, m);
}

// ---- Parte c)

type_n F67Iter(type_n n)
{
    // A: Caso base: n < 42
    if (n < 42)
    {
        return n;
    }

    // F: Valores iniciales
    type_n m = n % 7;
    type_n i = n;
    type_n t7 = 35 + m;
    type_n t14 = 28 + m;
    type_n t21 = 21 + m;
    type_n t28 = 14 + m;
    type_n t35 = 7 + m;
    type_n t42 = m;

    // B: Mientras no se llegue al caso base
    while (i >= ((n % 7) + 42))
    {
        // C: Calculo de F67(i)
        type_n f = t7 + t14 + t21 + t28 + t35 + t42;

        // D: Cambio de estado
        i -= 7;
        t42 = t35;
        t35 = t28;
        t28 = t21;
        t21 = t14;
        t14 = t7;
        t7 = f;
    }

    // B: Ya se calculo F67(n)
    return t7;
}

// ---- main

int main()
{
    type_n n = 100000;
    clock_t begin = clock();
    type_n out = F67Iter(n);
    clock_t end = clock();

    printf("%lu\n", out);
    printf("Elapsed %.5f miliseconds\n",
           1000 * ((double)(end - begin) / CLOCKS_PER_SEC));
    return 0;
}
