def do_operation(expression):
    a = int(expression[0])
    b = int(expression[2])
    if a > 10 or b > 10:
        raise Exception("Throws Exception")
    operator = expression[1]
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a // b
    else:
        raise Exception("Throws Exception")


def main(input: str):
    expression = input.split(' ')
    try:
        if len(expression) != 3:
            raise Exception("Throws Exception")
        if "." in expression[0] or "." in expression[2]:
            raise Exception("Throws Exception")
        print(do_operation(expression))
    except Exception as e:
        print(e)


main("10 - 5")
main("3 - 5")
main("3 * 5")
main("10 / 5")
main("9 / 5")
main("3 + 5")
main("6 + 5")
main("1")
main("1 + 2 1")
main("1 + 2 + 3")
main("3 ( 5")
main("11 - 5")
main("3 - 11")
main("1.0 - 5")
main("3 - 5.0")