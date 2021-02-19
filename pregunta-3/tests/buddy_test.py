from ..src.buddy import BuddySystem
import unittest


class TestBuddy(unittest.TestCase):
    def test_representacion(self):
        system = BuddySystem(120)
        system.allocate(16, 'A')
        system.allocate(1, 'B')
        representantion = system.representation()

        expected_representation = '\n-------- Bloques libres: \n'
        expected_representation += '(31,32) | 2 blocks\n'
        expected_representation += '(33,36) | 4 blocks\n'
        expected_representation += '(37,44) | 8 blocks\n'
        expected_representation += '(45,59) | 15 blocks\n'
        expected_representation += '(60,119) | 60 blocks\n'
        expected_representation += 'Total disponible: 89\n'
        expected_representation += '\n-------- Bloques reservados: \n'
        expected_representation += 'A | (0,29) | 30 blocks | 16 used blocks\n'
        expected_representation += 'B | (30,30) | 1 blocks | 1 used blocks\n'
        expected_representation += 'Total reservado: 31\n'

        self.assertEqual(representantion, expected_representation)

    def test_allocate(self):
        system = BuddySystem(120)
        out = system.allocate(16, 'A')

        self.assertEqual(out, 'Se reservaron 30 bloques para 16 bloques de A')
        self.assertTrue('A' in system.allocated)
        self.assertTrue(system.allocated['A'].size(), 16)

        out = system.allocate(1, 'A')

        self.assertEqual(
            out, 'Error: A ya se encuentra asignado a un bloque, por favor escoja un nombre distinto.')

        out = system.allocate(80, 'B')

        self.assertEqual(
            out, 'Error: no existe forma de almacenar 80 bloques sin quebrantar el BuddySystem. Memoria llena')
        self.assertFalse('B' in system.allocated)

    def test_deallocate(self):
        system = BuddySystem(120)

        out = system.deallocate('B')

        self.assertEqual(out, 'Error: "B" no esta reservado en el sistema.')

        system.allocate(16, 'A')
        system.allocate(1, 'B')
        system.allocate(28, 'C')
        system.allocate(28, 'D')

        out = system.deallocate('B')

        self.assertEqual(out, 'B liberado. Se liberaron 1 bloques')
        self.assertFalse('B' in system.allocated)
