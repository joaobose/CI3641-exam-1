from ..src.expression import ExpressionTree, postfixToExpressionTree, prefixToExpressionTree
import unittest


class TestBuddy(unittest.TestCase):
    def test_infix(self):
        expression = postfixToExpressionTree('8 3 - 8 4 4 + * +')
        infix = expression.infix()
        self.assertEqual(infix, '8 - 3 + 8 * (4 + 4)')

        # -- prueba de parentesis de precedencia

        expression = postfixToExpressionTree('5 3 * 5 1 + 2 / +')
        infix = expression.infix()
        self.assertEqual(infix, '5 * 3 + (5 + 1) / 2')

        # -- prueba de parentisis de asociatividad del -

        expression = postfixToExpressionTree('5 3 * 5 1 + -')
        infix = expression.infix()
        self.assertEqual(infix, '5 * 3 - (5 + 1)')

        expression = postfixToExpressionTree('5 3 * 5 -')
        infix = expression.infix()
        self.assertEqual(infix, '5 * 3 - 5')

        # -- prueba de parentisis de asociatividad del /

        expression = postfixToExpressionTree('10 2 5 / *')
        infix = expression.infix()
        self.assertEqual(infix, '10 * (2 / 5)')

        expression = postfixToExpressionTree('10 2 * 5 /')
        infix = expression.infix()
        self.assertEqual(infix, '10 * 2 / 5')

        expression = postfixToExpressionTree('10 2 / 5 /')
        infix = expression.infix()
        self.assertEqual(infix, '10 / 2 / 5')

        expression = postfixToExpressionTree('10 2 5 / /')
        infix = expression.infix()
        self.assertEqual(infix, '10 / (2 / 5)')

    def test_postfix(self):
        expression = postfixToExpressionTree('8 3 - 8 4 4 + * +')
        self.assertEqual(expression(), 69)

        expression = postfixToExpressionTree('5 3 * 5 1 + 2 / +')
        self.assertEqual(expression(), 18)

        expression = postfixToExpressionTree('5 3 * 5 1 + -')
        self.assertEqual(expression(), 9)

        expression = postfixToExpressionTree('5 3 * 5 -')
        self.assertEqual(expression(), 10)

        expression = postfixToExpressionTree('10 2 5 / *')
        self.assertEqual(expression(), 0)

        expression = postfixToExpressionTree('10 2 * 5 /')
        self.assertEqual(expression(), 4)

        expression = postfixToExpressionTree('10 2 / 5 /')
        self.assertEqual(expression(), 1)

        expression = postfixToExpressionTree('10 2 5 / /')
        with self.assertRaises(ZeroDivisionError):
            expression()

    def test_prefix(self):
        expression = prefixToExpressionTree('+ - 8 3 * 8 + 4 4')
        self.assertEqual(expression(), 69)

        expression = prefixToExpressionTree('+ * 5 3 / + 5 1 2')
        self.assertEqual(expression(), 18)

        expression = prefixToExpressionTree('- * 5 3 + 5 1')
        self.assertEqual(expression(), 9)

        expression = prefixToExpressionTree('- * 5 3 5')
        self.assertEqual(expression(), 10)

        expression = prefixToExpressionTree('* 10 / 2 5')
        self.assertEqual(expression(), 0)

        expression = prefixToExpressionTree('/ * 10 2 5')
        self.assertEqual(expression(), 4)

        expression = prefixToExpressionTree('/ / 10 2 5')
        self.assertEqual(expression(), 1)

        expression = prefixToExpressionTree('/ 10 / 2 5')
        with self.assertRaises(ZeroDivisionError):
            expression()
