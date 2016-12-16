def table(x,y):
    s=[]
    for number in range(1,y+1):
        a='{} * {} = {}'.format(x,number,x*number)
        s.append(a)
    return(s)  


