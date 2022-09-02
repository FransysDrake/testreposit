import datetime
import time

def formlist(n:int):
    list=[]
    a=0;
    while(a<=n):
        list.append(a)
        a+=1
    return list
a=formlist(15)
print(a)


def formlist1(n:int,type=None):
    list=[]
    a=0;
    while(a<=n):
        list.append(a)
        a+=1
    if (type==None):
        return list
    else:
        return tuple(list)

a=formlist1(15,"1")
print(a)



def recTime(func):
    def wrapper(*args,**kwargs):
        start=datetime.datetime.now()
        func(*args,**kwargs)
        done=datetime.datetime.now()-start
        print(f"Функция выполнена за {done}")
    return wrapper


@recTime
def formlist2(n:int,type=None):
    list=[]
    a=0;
    while(a<=n):
        list.append(a)
        a+=1
    if (type==None):
        return list
    else:
        return tuple(list)

formlist2(1000000,"1")
formlist2(1000000)
