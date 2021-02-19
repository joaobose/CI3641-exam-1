import math


class Partition:
    def __init__(self, lower, upper, relative_order):
        self.upper = upper
        self.lower = lower
        self.name = None
        self.used = None
        self.relative_order = relative_order

    def size(self):
        return self.upper - self.lower + 1

    def representation(self):
        out = f'{self.name} | ' if self.name != None else ''
        out += f'({self.lower},{self.upper}) | {self.size()} blocks'
        out += f' | {self.used} used blocks' if self.used != None else ''
        return out


class BuddySystem:
    def __init__(self, size):
        self.size = size

        # Maxima potencia de 2
        self.n = self.order(self.size)

        # Lista de particiones
        # Las guardamos por orden de potencias de dos
        # Agregamos un elemento mas para poder indexar con log2
        # self.partitions[i] contiene las particiones de tamaño proporcional a 2^i
        self.partitions = [[] for x in range(self.n + 1)]

        # Diccionario de particiones reservadas
        self.allocated = {}

        # Inicialmente existe una sola particion, la mas grande posible
        self.partitions[self.n].append(Partition(0, self.size - 1, self.n))

    def order(self, size):
        return math.ceil(math.log2(size))

    def allocate(self, size, name):
        # Verificamos que el nombre no este referenciado
        if name in self.allocated:
            return self.__allocation_conflict(name)

        order = self.order(size)

        # Si tenemos al menos una particion adecuada
        if len(self.partitions[order]) > 0:
            discarted = []
            selected = self.partitions[order].pop()

            # seleccionamos aquella que admita el tamaño adecuado
            while len(self.partitions[order]) > 0 and selected.size() < size:
                discarted.append(selected)
                selected = self.partitions[order].pop()

            self.partitions[order] += discarted

            # Si la mejor particion admite los bloques necesarios
            if selected.size() >= size:
                return self.__allocation_success(selected, name, size)
            else:
                # Si no, la descartamos
                self.partitions[order].append(selected)

        # No existe una particion adecuada

        # Particionaremos la particion ya existente de orden superior mas pequeña

        # Obtenemos los orderes superiores con particiones disponibles
        biggerOrders = [i for i in range(
            order, self.n + 1) if len(self.partitions[i]) > 0]

        # Si no hay bloques de orden superior para particionar
        # Memoria llena
        if len(biggerOrders) == 0:
            return self.__allocation_failed(size)

        # Obtenemos el orden de la particion a particionar
        biggerOrder = biggerOrders[0]

        # Obtenemos la particion en cuestion
        selected = self.partitions[biggerOrder].pop()

        # Particionamos hasta tener una particion adecuada
        while biggerOrder > order and (selected.size() // 2) >= size:
            biggerOrder -= 1

            # Particionamos mitad y mitad
            lowerHalf = Partition(
                selected.lower, selected.lower + (selected.size() // 2) - 1, selected.relative_order - 1)
            upperHalf = Partition(
                selected.lower + (selected.size()) // 2, selected.upper, selected.relative_order - 1)

            # Seleccionamos la mitad adecuada
            if size <= lowerHalf.size():
                self.partitions[biggerOrder].append(upperHalf)
                selected = lowerHalf
            else:
                self.partitions[biggerOrder].append(lowerHalf)
                selected = upperHalf

        # La mejor particion esta en el mismo orden lo que lo quiere reservar

        # Si la mejor particion no puede contener lo solicitado
        if selected.size() < size:
            # Retornamos error
            self.partitions[order].append(selected)
            return self.__allocation_failed(size)

        # Ya tenemos la particion adecuada, asi que la reservamos
        return self.__allocation_success(selected, name, size)

    def deallocate(self, name):
        # Verificamos que el nombre este referenciado
        if not name in self.allocated:
            return self.__deallocation_failed(name)

        # Liberamos la particion
        deallocated = self.allocated[name]
        del self.allocated[name]
        deallocated.used = None
        deallocated.name = None

        # Hacemos merge de buddies si es necesario

        lost = deallocated
        while lost != None:
            current_order = lost.relative_order

            # buscamos los posibles buddies
            posibleBuddies = [i for i in range(0, len(self.partitions[current_order]))
                              if self.partitions[current_order][i].upper == lost.lower - 1
                              or self.partitions[current_order][i].lower == lost.upper + 1]

            # Si no hay posibles buddies, no hay nada por hacer
            if len(posibleBuddies) == 0:
                self.partitions[current_order].append(lost)
                break

            # Sabemos que si existe un buddy, es uno solo
            buddy = self.partitions[current_order].pop(posibleBuddies[0])

            # Hacemos merge
            merged = Partition(0, 0, lost.relative_order + 1)
            if buddy.upper == lost.lower - 1:
                merged.lower = buddy.lower
                merged.upper = lost.upper
            elif buddy.lower == lost.upper + 1:
                merged.lower = lost.lower
                merged.upper = buddy.upper

            lost = merged

        return self.__deallocation_success(deallocated, name)

    def representation(self):
        return self.__free_blocks_representation() + self.__allocated_blocks_representation()

    def __free_blocks_representation(self):
        out = '\n-------- Bloques libres: \n'
        memory = 0
        for order in self.partitions:
            for partition in order:
                out += f'{partition.representation()}\n'
                memory += partition.size()

        out += f'Total disponible: {memory}\n'
        return out

    def __allocated_blocks_representation(self):
        out = '\n-------- Bloques reservados: \n'
        memory = 0
        for partition in self.allocated.values():
            out += f'{partition.representation()}\n'
            memory += partition.size()

        out += f'Total reservado: {memory}\n'
        return out

    def __allocation_success(self, partition, name, size):
        partition.name = name
        partition.used = size
        self.allocated[name] = partition
        return f'Se reservaron {partition.size()} bloques para {size} bloques de {name}'

    def __allocation_conflict(self, name):
        return f'Error: {name} ya se encuentra asignado a un bloque, por favor escoja un nombre distinto.'

    def __allocation_failed(self, size):
        return f'Error: no existe forma de almacenar {size} bloques sin quebrantar el BuddySystem. Memoria llena'

    def __deallocation_failed(self, name):
        return f'Error: "{name}" no esta reservado en el sistema.'

    def __deallocation_success(self, partition, name):
        return f'{name} liberado. Se liberaron {partition.size()} bloques'
