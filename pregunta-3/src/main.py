from .buddy import BuddySystem

n = int(input('Ingrese el numero de bloques de memoria a manejar: '))

system = BuddySystem(n)

while True:
    args = input("Introduzca su comando: ").split()

    command = args[0]

    if command == 'SALIR':
        break

    if command == 'MOSTRAR':
        print(system.representation())
        continue

    if command == 'RESERVAR':
        name = args[1]
        size = int(args[2])
        print(system.allocate(size, name))
        continue

    if command == 'LIBERAR':
        name = args[1]
        print(system.deallocate(name))
        continue
