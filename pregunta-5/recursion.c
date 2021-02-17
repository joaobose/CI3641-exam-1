
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

// n = 42 => F(35) + F(28) + F(21) + F(14) + F(7) + F(0)
// n = 43 => F(36) + F(29) + F(22) + F(15) + F(8) + F(1)
// n = 44 => F(37) + F(30) + F(23) + F(16) + F(9) + F(2)
// n = 45 => F(38) + F(31) + F(24) + F(17) + F(10) + F(3)
// n = 46 => F(39) + F(32) + F(25) + F(18) + F(11) + F(4)
// n = 47 => F(40) + F(33) + F(26) + F(19) + F(12) + F(5)
// n = 48 => F(41) + F(34) + F(27) + F(20) + F(13) + F(6)
//
// n = 49 => F(42) + F(35) + F(28) + F(21) + F(14) + F(7)
// n = 50 => F(43) + F(36) + F(29) + F(22) + F(15) + F(8)
// n = 51 => F(44) + F(37) + F(30) + F(23) + F(16) + F(9)
// n = 52 => F(45) + F(38) + F(31) + F(24) + F(17) + F(10)
// n = 53 => F(46) + F(39) + F(32) + F(25) + F(18) + F(11)
// n = 54 => F(47) + F(40) + F(33) + F(26) + F(19) + F(12)
// n = 55 => F(48) + F(41) + F(34) + F(27) + F(20) + F(13)
//
// n = 56 => F(49) + F(42) + F(35) + F(28) + F(21) + F(14)
// ...
//
//        7          14        21        28        35       42
// F(n) = ANTERIOR + PRIMERO + SEGUNDO + TERCERO + CUARTO + QUINTO
// ANTERIOR = F(n)
// PRIMERO = ANTERIOR
// SEGUNDO = PRIMERO
// TERCERO = SEGUNDO
// CUARTO = TERCERO
// QUINTO = CUARTO
//

type_n F67TailHelper(type_n n, type_n i, type_n t7, type_n t14, type_n t21, type_n t28, type_n t35, type_n t42)
{
    if (n < 42)
    {
        return n;
    }

    if (i < ((n % 7) + 42))
    {
        return t7;
    }

    type_n f = t7 + t14 + t21 + t28 + t35 + t42;
    return F67TailHelper(n, i - 7, f, t7, t14, t21, t28, t35);
}

type_n F67Tail(type_n n)
{
    type_n m = n % 7;
    return F67TailHelper(n, n, 35 + m, 28 + m, 21 + m, 14 + m, 7 + m, m);
}

// ---- Parte c)

type_n F67Iter(type_n n)
{
    if (n < 42)
    {
        return n;
    }

    type_n m = n % 7;
    type_n i = n;
    type_n t7 = 35 + m;
    type_n t14 = 28 + m;
    type_n t21 = 21 + m;
    type_n t28 = 14 + m;
    type_n t35 = 7 + m;
    type_n t42 = m;

    while (i >= ((n % 7) + 42))
    {
        type_n f = t7 + t14 + t21 + t28 + t35 + t42;
        i -= 7;
        t42 = t35;
        t35 = t28;
        t28 = t21;
        t21 = t14;
        t14 = t7;
        t7 = f;
    }

    return t7;
}

// ---- main

int main()
{
    type_n n = 260;
    clock_t begin = clock();
    type_n out = F67(n);
    clock_t end = clock();

    printf("%lu\n", out);
    printf("Elapsed %.5f miliseconds\n",
           1000 * ((double)(end - begin) / CLOCKS_PER_SEC));
    return 0;
}
