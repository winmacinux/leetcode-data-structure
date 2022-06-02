import operator

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "^": operator.xor
}


def evaluatePostfixExpression(E=[]):

    # Initialization
    stack = []

    assert len(E), "No expression detected"

    for value in E:
        # Check Operand
        print(value, stack, len(stack))
        if isinstance(value, int):
            stack.append(int(value))
            pass
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(operators[value](b, a))
            pass
        pass

    return stack.pop()


if __name__ == "__main__":
    try:
        E = [5, 6, 2, "+", "*", 12, 4, "/", "-"]
        result = evaluatePostfixExpression(E)
        print("Result:", result)
    except AssertionError as e:
        print("Error:", e.__str__())
