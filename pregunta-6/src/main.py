from .expression import ExpressionTree, postfixToExpressionTree, prefixToExpressionTree


while True:
    args = input("Introduzca su comando: ").split()

    command = args[0]

    if command == 'SALIR':
        break

    if command == 'EVAL':
        orden = args[1]
        expression = ' '.join(args[2:])
        if orden == 'PRE':
            print(prefixToExpressionTree(expression)())
        elif orden == 'POST':
            print(postfixToExpressionTree(expression)())
        continue

    if command == 'MOSTRAR':
        orden = args[1]
        expression = ' '.join(args[2:])
        if orden == 'PRE':
            print(prefixToExpressionTree(expression).infix())
        elif orden == 'POST':
            print(postfixToExpressionTree(expression).infix())
        continue
