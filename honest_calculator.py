msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

operation = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y}


def is_one_digit(v):
    return True if -10 < v < 10 and type(v) is int else False


def check(v1, v2, v3):
    msg = ""
    msg += msg_6 if is_one_digit(v1) and is_one_digit(v2) else ""
    msg += msg_7 if v1 == 1 or v2 == 1 and v3 == "*" else ""
    msg += msg_8 if v1 == 0 or v2 == 0 and v3 in ['+', '*', '-'] else ""
    print(msg_9 + msg) if msg != "" else ""


def is_int(n):
    return int(n) if float(n).is_integer() else float(n)


def start():
    memory = 0
    while True:
        calc = input(msg_0)
        x, oper, y = calc.split()
        try:
            x = memory if x == 'M' else float(x)
            y = memory if y == 'M' else float(y)
            check(is_int(x),is_int(y), oper)
            result = operation[oper](x, y)
            print(float(result))
            if input(msg_4) == 'y':
                if is_one_digit(is_int(result)):
                    msg_index = 10
                    while True:
                        answer = input(globals()[f'msg_{msg_index}'])
                        if answer == 'y':
                            if msg_index < 12:
                                msg_index += 1
                            else:
                                memory = result
                                break
                        elif answer == 'n':
                            break
                else:
                    memory = result
            if input(msg_5) == 'n':
                break
        except ValueError:
            print(msg_1)
        except KeyError:
            print(msg_2)
        except ZeroDivisionError:
            print(msg_3)


if __name__ == '__main__':
    start()

