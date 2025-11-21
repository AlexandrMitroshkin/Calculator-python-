import sys

user_input = input("Введите выражение: ")
common_expr = user_input.split()
expr = []

for i in common_expr:
    if i.isdigit() or (i[0] == '-' and i[1:].isdigit()):
        expr.append(int(i))
    elif i in '+-*/()': 
        expr.append(i)


                                                  
def summ(act_index, list_expr):
    left = list_expr[act_index-1]
    right = list_expr[act_index+1]   
    list_expr[act_index+1] = left + right
    del list_expr[act_index - 1]
    del list_expr[act_index - 1]

def diff(act_index, list_expr):
    left = list_expr[act_index-1]
    right = list_expr[act_index+1]
    list_expr[act_index+1] = left - right
    del list_expr[act_index - 1]
    del list_expr[act_index - 1]

def mult(act_index, list_expr):
    left = list_expr[act_index-1]
    right = list_expr[act_index+1]
    list_expr[act_index+1] = left * right
    del list_expr[act_index - 1]
    del list_expr[act_index - 1]

def div(act_index, list_expr):
    left = list_expr[act_index-1]
    right = list_expr[act_index+1]
    if right == 0:
        print("Ошибка: деление на ноль")
        sys.exit()
    else:
        list_expr[act_index+1] = left / right
        del list_expr[act_index - 1]
        del list_expr[act_index - 1]


def operation(expr):
    if len(expr) == 1:
        if type(expr[0]) == int or type(expr[0]) == float:
            return expr[0] 
        else:
            return "Ошибка: одиночный оператор"
        
    if "(" in expr:
        brace_operation(expr)
    
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

def brace_operation(expr):
    brace_dict = {}
    for i in range(len(expr)):
        if expr[i] == "(":
            if len(brace_dict) == 0:
                brace_dict["br1"] = {
                    "status": "untaken",
                    "pair": 1,
                    "depth": 0,
                    "index" : i,
                }
            elif len(brace_dict) > 0:
                comparsion_pair = []
                current_depth = 0
                for brace in brace_dict.keys():
                    if brace_dict[brace]["status"] == 'untaken':
                        current_depth += 1
                    comparsion_pair.append(brace_dict[brace]["pair"])

                the_biggest_pair = max(comparsion_pair)           

                brace_dict['br' + str(the_biggest_pair + 1)] = {
                    "status": "untaken",
                    "pair": the_biggest_pair + 1,
                    "depth": current_depth,
                    "index" : i,
                }    

        if expr[i] == ")":            
            if len(brace_dict) == 1:
                brace_dict["br1_cl"] = {
                    "status": "taken",
                    "pair": 1,
                    "depth": 0,
                    "index" : i,
                }

                brace_dict["br1"]["status"] = "taken"

            elif len(brace_dict) > 0:

                list_of_pairs = []
                for item in brace_dict.keys():
                    if brace_dict[item]["status"] == "untaken":
                        list_of_pairs.append(brace_dict[item]["pair"])
                max_untaken_pair = max(list_of_pairs)

                for item in brace_dict.keys():
                    if brace_dict[item]["pair"] == max_untaken_pair:
                        pair_open_key = item 
                        break

                brace_dict["br" + str(max_untaken_pair) + "_cl"] = {
                    "status": "taken",
                    "pair": max_untaken_pair,
                    "depth": brace_dict[pair_open_key]["depth"],
                    "index" : i,
                }
                brace_dict[pair_open_key]["status"] = "taken"

    newExpr = expr
    depth_list = []

    for i in brace_dict.keys():
        depth_list.append(brace_dict[i]["depth"])

    while len(depth_list) > 1:

        keys_list = list(brace_dict.keys())

        the_deepest_number = max(depth_list)
        for action in keys_list: 
            if brace_dict[action]["depth"] == the_deepest_number:
                if newExpr[brace_dict[action]['index']] == "(":
                    open_brace = action
                else :
                    close_brace = action
                    break

        temporary_list = (newExpr[brace_dict[open_brace]['index'] + 1:brace_dict[close_brace]['index']])
        len_temporary_list = len(temporary_list)
        newExpr = newExpr[:brace_dict[open_brace]['index']] + newExpr[brace_dict[close_brace]['index'] + 1:]
        newExpr.insert(brace_dict[open_brace]['index'] , operation(temporary_list))

        brace_open_index = brace_dict[open_brace]['index']

        temporary_counter = 0
        while temporary_counter  < 2:
            del depth_list[the_deepest_number]
            temporary_counter += 1
        del brace_dict[open_brace]
        del brace_dict[close_brace]
        keys_list.remove(open_brace)
        keys_list.remove(close_brace)

        for brace in keys_list:
            if brace_dict[brace]['index'] >= brace_open_index:
                brace_dict[brace]['index'] -= len_temporary_list + 1

    if len(brace_dict) == 0:
        return(operation(newExpr))


def inspection(expr):
    brece_list = []
    brace_exist = False
    if len(expr) == 0:
        print("Пустое выражение")
        return

    for i in range(len(expr)):
        if type(expr[i]) == str and expr[i] != "(" and expr[i] != ")":
            if i == 0 or i == len(expr)-1:
                print("Ошибка: оператор в начале или конце")
                return
            if (type(expr[i-1]) != int and expr[i-1] not in ("(", ")")) or (type(expr[i+1]) != int and expr[i+1] not in ("(", ")")):
                print("Ошибка: рядом с оператором нет чисел")
                return
        if expr[i] == "(":
            brace_exist = True
            brece_list.append(expr[i])
        if expr[i] == ")":
            brace_exist = True
            if len(brece_list) == 0:
                print("Ошибка несоответствие скобок")
                sys.exit()
            else:
                brece_list.pop()
         
    if brace_exist and len(brece_list) != 0:
        print("Ошибка: несоответствие скобок")
        sys.exit()

    if brace_exist:
        for braceItem in range(len(expr) - 1):
            if expr[braceItem] == "(" and expr[braceItem + 1] == ")":
                print("Ошибка: пустые скобки")
                sys.exit()
        
        if "(" in expr and ")" not in expr or ")" in expr and "(" not in expr:
            print("Ошибка несоответствие скобок")
            sys.exit()
    
    if brace_exist == False:
        print("Ответ:" , operation(expr))   
    elif brace_exist == True:
        print("Ответ:" , brace_operation(expr))
    else: 
        print("Ошибка несоответствие скобок")

print("Правила ввода:" \
     "Вводить всё только через пробелы , любой символ должке быть отделен от другого пробелом;" \
     "Деление на ноль запрещено;" \
     "Выражения должны быть написаны грамтно , пример не правильного ввода: + + -19 / 1 ) " \
     "Пример правильного ввода: 7 * ( ( 10 + 2 ) - ( 2 * 6 ) )")

inspection(expr)