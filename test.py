def do_operation(expression):
    a = int(expression[0])
    b = int(expression[2])
    if a < 1 or a > 10 or b < 1 or b > 10:
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
        return str(do_operation(expression))
    except Exception as e:
        return e


if __name__ == '__main__':
    is_cycle = True
    while is_cycle:
        expr = input("Enter math expression please: ")
        print(main(expr))
        exit_cycle = input("Press 1 to exit: ")
        if exit_cycle == "1":
            is_cycle = False
print(main("3 - 5"))
print(main("3 * 5"))
print(main("10 / 5"))
print(main("9 / 5"))
print(main("3 + 5"))
print(main("6 + 5"))
print(main("1"))
print(main("1 + 2 1"))
print(main("1 + 2 + 3"))
print(main("3 ( 5"))
print(main("11 - 5"))
print(main("3 - 11"))
print(main("1.0 - 5"))
print(main("3 - 5.0"))
