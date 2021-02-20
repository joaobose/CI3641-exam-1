
def isOperator(x):
    return x == '+' or x == '-' or x == '*' or x == '/'


def hasLowestPrecedence(x):
    return x == '+' or x == '-'


def hasHighestPrecedence(x):
    return x == '*' or x == '/'


# Representamos una expresion como un arbol binario.
# Esto porque todos lo operadores soportados son binarios.
class ExpressionTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def infix(self):
        # Los nodos hojas son numeros
        if self.right is None and self.left is None:
            return f'{self.value}'

        leftExp = self.left.infix()
        ownExp = f'{self.value}'
        rightExp = self.right.infix()

        if hasHighestPrecedence(ownExp):
            # Check de menor precedencia izquierda
            if hasLowestPrecedence(self.left.value):
                leftExp = f'({leftExp})'

            # Check de menor precedencia derecha
            # Check de asociatividad del (/)
            if hasLowestPrecedence(self.right.value) or self.right.value == '/':
                rightExp = f'({rightExp})'

        # Check de asociatividad del (-)
        elif ownExp == '-':
            if hasLowestPrecedence(self.right.value):
                rightExp = f'({rightExp})'

        return f'{leftExp} {ownExp} {rightExp}'

    def __call__(self):
        # Los nodos hojas son numeros
        if self.left is None and self.right is None:
            return self.value

        # Evaluamos izquierda y derecha
        leftEval = self.left()
        rightEval = self.right()

        # Operamos izquierda y derecha
        if self.value == '+':
            return leftEval + rightEval

        if self.value == '-':
            return leftEval - rightEval

        if self.value == '*':
            return leftEval * rightEval
        else:
            return leftEval // rightEval


# Construye un ExpressionTree a partir de una expresion en postfix
def postfixToExpressionTree(postfix):
    # Utilizamos un stack
    stack = []

    # Iteramos por cada caracter de la expresion
    for char in postfix.strip().split(' '):
        # Caso: es un un numero
        if not isOperator(char):
            # Agregamos al stack un nodo hoja
            stack.append(ExpressionTree(int(char)))

        # Caso: es un operador
        else:
            # Creamos un nodo operador
            operator = ExpressionTree(char)

            # Como estamos es postfix, los operandos son los dos operandos calculados mas recientemente
            right = stack.pop()
            left = stack.pop()
            operator.right = right
            operator.left = left

            # Agregamos el nodo al stack
            stack.append(operator)

    # Retornamos la expresion mas reciente
    # Es decir, la padre
    return stack.pop()


# Construye un ExpressionTree a partir de una expresion en prefix
def prefixToExpressionTree(prefix):
    # Funcion auxiliar que obtiene el ExpressionTree de un expression (en prefix) comenzando en el indice start
    # Retorna el ExpressionTree (de existir) y el indice en donde termina dicho ExpressionTree.
    def parse(expression, start):
        # Si hay overflow retornamos None
        if start >= len(expression):
            return None, start

        # Obtenemos el primero caracter
        char = expression[start]

        # Caso: es un numero
        if not isOperator(char):
            # Retornamos un nodo hoja
            return ExpressionTree(int(char)), start
        # Caso: es un operador
        else:
            # Hacemos parse de la expresion de la izquierda
            (leftExp, leftEnd) = parse(expression, start + 1)

            # Hacemos parse de la expresion de la derecha (a partir de donde termino leftExp)
            (rightExp, rightEnd) = parse(expression, leftEnd + 1)

            # Creamos el nodo operador
            currentExp = ExpressionTree(char)
            currentExp.left = leftExp
            currentExp.right = rightExp

            # Retornamos el nodo operador junto con el indice donde termina
            return currentExp, rightEnd

    (tree, _) = parse(prefix.strip().split(' '), 0)
    return tree
