def gen_fib(n,a=0,b=1):
    if n==0:
        return
    if n==1:
        return 0
    print(a,b,end=" ")
    for i in range(3,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
