# --- Parte a)


def zip(a, b):
    if a and b:
        yield (a[0], b[0])
        for p in zip(a[1:], b[1:]):
            yield p


# for p in zip([1, 2, 3], ['a', 'b', 'c']):
#     print(p)


def zipWith(a, b, f):
    if a and b:
        yield f(a[0], b[0])
        for p in zipWith(a[1:], b[1:], f):
            yield p


# for p in zipWith([0, 1, 2, 1], [1, 2, 1, 0], lambda x, y: x + y):
#     print(p)


# --- Parte b)

def misterio(p):
    yield p
    acum = []
    for p in zipWith([0, *p], [*p, 0], lambda x, y: x + y):
        acum += [p]

    for m in misterio(acum):
        yield m


# for m in misterio([1]):
#     print(m)


def suspenso(p):
    for m in p:
        yield m
    acum = []
    for p in zipWith([0, *p], [*p, 0], lambda x, y: x + y):
        acum += [p]
    for m in suspenso(acum):
        yield m


# for m in suspenso([1]):
#     print(m)
