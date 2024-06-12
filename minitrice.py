import sys

def calculate(expression):
    try:
        if '+' in expression:
            operands = expression.split('+')
            result = float(operands[0]) + float(operands[1])
        elif '-' in expression:
            operands = expression.split('-')
            result = float(operands[0]) - float(operands[1])
        elif '*' in expression:
            operands = expression.split('*')
            result = float(operands[0]) * float(operands[1])
        elif '/' in expression:
            operands = expression.split('/')
            if float(operands[1]) == 0:
                return "Division par zéro", 1
            result = float(operands[0]) / float(operands[1])
        else:
            return f"Erreur de syntaxe pour le calcul: {expression}", 1
        return f"{result:.2f}", 0
    except Exception:
        return f"Erreur de syntaxe pour le calcul: {expression}", 1

if __name__ == "__main__":
    if len(sys.argv) == 1:
        while True:
            try:
                expression = input("> ")
                result, code = calculate(expression)
                print(result)
                if code == 1:
                    sys.exit(1)
            except EOFError:
                print("Fin des calculs")
                sys.exit(0)
    else:
        for line in sys.stdin:
            result, code = calculate(line.strip())
            print(result)
            if code == 1:
                sys.exit(1)
