import natural as f1
def POZ_Z_D(mas): # на вход функция получает целое число
    # Семёнов Михаил
    # Знак целого числа
    if mas[0] == '1': # первый символ числа "-"
        res = 1
    elif mas[0] == '0': # число равно нулю
        res=0
    else : #число положительное
        res = 2
    return res

def ABS_Z_N(celoe):
    # Семёнов Михаил
    # Модуль целого числа
    if POZ_Z_D(celoe) == '-':
        return celoe[1:]
    else:
        return celoe

def SUB_ZZ_Z(list1, list2):
    # Семёнов Михаил
    # Вычитание целых чисел
    if POZ_Z_D(list1) == '+' and POZ_Z_D(list2) == '-':
        return f1.ADD_NN_N(list1, ABS_Z_N(list2))
    elif POZ_Z_D(list1) == '-' and POZ_Z_D(list2) !='-':
        if POZ_Z_D(list2) == '+':
            return ['-'] + f1.ADD_NN_N(ABS_Z_N(list1), ABS_Z_N(list2))
        else :
            return  list1
    
    elif f1.COM_NN_D(ABS_Z_N(list1), ABS_Z_N(list2)) == 2 :
        if list2 != 0:
            return f1.SUB_NN_N(ABS_Z_N(list1), ABS_Z_N(list2))
        else :
            return list1
    elif POZ_Z_D(list1) == 0 :
        if POZ_Z_D(list2) == '-':
            return list2[1:]
        elif list2 == [0]:
            return list2
        else :
            return ['-'] + list2

    else:
        if POZ_Z_D(list1) == '+':
            return ['-'] + f1.SUB_NN_N(ABS_Z_N(list2), ABS_Z_N(list1))
        else :
            return  f1.SUB_NN_N(ABS_Z_N(list2), ABS_Z_N(list1))
  
    
    

def ADD_ZZ_Z(b1, n1, list1, b2, n2, list2):
    #Дашкин Дамир
    #Сложение целых чисел
    str1 = ""
    str2 = ""
    for i in range(len(list1)):
        str1 = str1 + str(list1[i])
    for j in range(len(list2)):
        str2 = str2 + str(list2[j])
    if b1 == 1:
        str1 = "-" + str1
    num1 = int(str1)
    if b2 == 1:
        str2 = "-" + str2
    num2 = int(str2)
    if f1.POZ_Z_D(num1) == 2 and f1.POZ_Z_D(num2) == 2:
        res = f1.ADD_NN_N(num1, num2)
    if f1.POZ_Z_D(num1) == 1 and f1.POZ_Z_D(num2) == 1:
        mod1 = f1.ABS_Z_N(num1)
        mod2 = f1.ABS_Z_N(num2)
        res = f1.ADD_NN_N(mod1, mod2)
        res = f1.MUL_ZM_Z(res)
    else:
        mod1 = f1.ABS_Z_N(num1)
        mod2 = f1.ABS_Z_N(num2)
        if f1.COM_NN_D(mod1, mod2) == 2:
            if f1.POZ_Z_D(num1) == 1:
                res = f1.SUB_NN_N(mod1, mod2)
                res = f1.MUL_ZM_Z(res)
            else:
                res = f1.SUB_NN_N(mod1, mod2)
        if f1.COM_NN_D(mod1, mod2) == 1:
            if f1.POZ_Z_D(num2) == 1:
                res = f1.SUB_NN_N(mod2, mod1)
                res = MUL_ZM_Z(res)
            else:
                res = f1.SUB_NN_N(mod2, mod1)
        else:
            res = 0
    return res
  
def MOD_ZZ_Z(b1, n1, list1, b2, n2, list2):
    #Дашкин Дамир
    #Остаток от деления целых чисел
    str1 = ""
    str2 = ""
    for i in range(len(list1)):
        str1 = str1 + str(list1[i])
    for j in range(len(list2)):
        str2 = str2 + str(list2[j])
    if b1 == 1:
        str1 = "-" + str1
    num1 = int(str1)
    if b2 == 1:
        str2 = "-" + str2
    num2 = int(str2)
    q = DIV_ZZ_Z(num1, num2)
    k = MUL_ZZ_Z(q, num2)
    res = SUB_ZZ_Z(num1, k)
    return res


