def fizzbizz(n):
    s=[]
    for i in range(1,n+1):
        if i % 15==0:
           a="fizzbizz"
           s.append(a)
        elif i % 5==0:
           b="bizz"
           s.append(b)
        elif i % 3==0:
           c="fizz"
           s.append(c)
        else:
           d=i
           s.append(d)
    return(s)

