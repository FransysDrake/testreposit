def calc(a:int, b:int, type):
    try:
        if (type=='+'):
           print(a+b)
        elif (type=='-'):
            print(a - b)
        elif (type=='*'):
            print(a * b)
        elif (type=='/'):
            print(a / b)
        else:
            print("Неподдерживаемое действие")
    except ZeroDivisionError:
        print("Ошибка деления на ноль")
    except ValueError:
        print("Вводите корректные значения")
    except Exception as e:
        print( e.type(e))
    finally:
        print("Конец")


calc(2,5,"-")
calc(20,5,"*")
calc(2,0,"/")
calc(2,5,"+")
calc(2,0,"2222")