user_input = input("Введите выражение: ")
common_expression = user_input.split()
expression = []
result = 0
indicator = 0

def is_action(x):
    if type(x) == str:
        return True
    else :
        return False
    
for i in common_expression:
    if i.lstrip('-').isdigit():
        expression.append(int(i))
    elif i == "+" or i == "-":
        expression.append(i)

def summa(action_position, list_expression):
    left = list_expression[action_position-1]
    right = list_expression[action_position+1]
    list_expression[action_position+1] = left + right
    list_expression.remove(list_expression[action_position])
    list_expression.remove(left)


def difference(action_position, list_expression):
    left = list_expression[action_position-1]
    right = list_expression[action_position+1]
    list_expression[action_position+1] = left - right
    list_expression.remove(list_expression[action_position])
    list_expression.remove(left)


def recyrsia(counter , list_expression):
    global result
    global indicator
    if counter == 1:
        if list_expression[1] == '+':
            result += list_expression[0] + list_expression[2]
            indicator += 1
        elif expression[1] == '-':
            result += list_expression[0] - list_expression[2]
            indicator += 1
    elif counter != 1:
        for i in list_expression:
            if is_action(i):
                if i == "+":
                    summa(list_expression.index(i), list_expression)
                    counter -= 1
                    recyrsia(counter , list_expression)
                elif i == "-":
                    difference(list_expression.index(i), list_expression)
                    counter -= 1
                    recyrsia(counter , list_expression)
    return result

def operation():
    global result
    global indicator
    for i in expression:
        if len(expression) == 1 and type(i) != str:
            result =  expression[0]
            return result
        elif len(expression) == 1 and type(i) == str:
            return "Неправильный синтаксис, попробуйте еще раз"
        elif len(expression) != 1:
            counter_actions = 0
            for item in expression:
                if is_action(item):
                    counter_actions += 1
            if indicator == 0:
                recyrsia(counter_actions , expression)
            else:
                return result
            
print(operation())