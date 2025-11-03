user_input = input("Введите выражение: ")
common_expr = user_input.split()
expr = []

for i in common_expr:
    if i.lstrip('-').isdigit():
        expr.append(int(i))
    elif i.lstrip('(').isdigit() or i.rstrip(')').isdigit():
        if i == '(' or i == ')':
            expr.append(i)
        if len(i) > 1:
            if i[0] == '(':
                expr.append('(')
                expr.append(int(i[1:]))
            elif i[-1] == ')':
                expr.append(int(i[:-1]))
                expr.append(')')
    elif i == "+" or i == "-" or i == "*" or i == "/" or i =='(' or i == ')':
        expr.append(i)

                                                  
def summ(act_index, list_expr):
    left = list_expr[act_index-1]
    right = list_expr[act_index+1]   
    list_expr[act_index+1] = left + right
    del list_expr[act_index]
    del list_expr[list_expr.index(left)]

def diff(act_index, list_expr):
    left = list_expr[act_index-1]
    right = list_expr[act_index+1]
    list_expr[act_index+1] = left - right
    del list_expr[act_index]
    del list_expr[list_expr.index(left)]

def mult(act_index, list_expr):
    left = list_expr[act_index-1]
    right = list_expr[act_index+1]
    list_expr[act_index+1] = left * right
    del list_expr[act_index]
    del list_expr[list_expr.index(left)]

def div(act_index, list_expr):
    left = list_expr[act_index-1]
    right = list_expr[act_index+1]
    list_expr[act_index+1] = left / right
    del list_expr[act_index]
    del list_expr[list_expr.index(left)]


def operation(expr):
    if len(expr) == 1:
        if type(expr[0]) == int or float:
            return expr[0] 
        else:
            return "Ошибка: одиночный оператор"
        
    for i in expr:
        if type(i) == str:
            if i == "*":
                mult(expr.index(i), expr)
                return operation(expr)
            elif i == "/":
                div(expr.index(i), expr)
                return operation(expr)  
            
    for item in expr:
        if type(item) == str:
            if item == "+":
                summ(expr.index(item), expr)
                return operation(expr)
            elif item == "-":
                diff(expr.index(item), expr)
                return operation(expr)
    return "Ошибка: нет операторов"

# def brace_operation(expr):
#     brace_dict = {}
#     newExpr = []
#     for i in range(len(expr)):
#         if expr[i] == "(":
#             if len(brace_dict) == 0:
#                 brace_dict["br1"] = {
#                     "status": "untaken",
#                     "pair": 1,
#                     "depth": 0,
#                     "index" : i
#                 }

def inspection(expr):
    brece_list = []
    if len(expr) == 0:
        print("Пустое выражение")
        return

    for i in range(len(expr)):
        if type(expr[i]) == str and expr[i] != "(" and expr[i] != ")":
            if i == 0 or i == len(expr)-1:
                print("Ошибка: оператор в начале или конце")
                return
            if type(expr[i-1]) != int and expr[i-1] not in ("(", ")") or type(expr[i+1]) != int and expr[i-1] not in ("(", ")"):
                print("Ошибка: рядом с оператором нет чисел")
                return
        if expr[i] == "(":
            brece_list.append(expr[i])
        if expr[i] == ")":
            if len(brece_list) == 0:
                print("Ошибка несоответствие скобок")
            else:
                brece_list.pop()
    
    if len(brece_list) == 0:         
        result = operation(expr)
        print(result)

    else: 
        print("Ошибка несоответствие скобок")
inspection(expr)

