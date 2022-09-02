import statistics


def averfunc(*args):
    print(round(statistics.mean(args),2))


averfunc(21,14,35,117)

def maxminnum(*args):
    print("Если хотите найти максимальное, нажмите 1,если минимальное -2 ")
    x=int(input())
    if(x==1):
        a=sorted(args)
        print(a[len(a)-1])
    elif(x==2):
        a=sorted((args),reverse=True)
        print(a[0])
    else:
        print("введено некорректное значение")

maxminnum(14,22.2,0,15)
