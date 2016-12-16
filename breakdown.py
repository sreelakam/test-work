def change(money):
    s=[]
    for i in [1000,500,100,50,20,10,1]:
        denom= money/i
        if denom>0:
           a='{} * {} = {}'.format(i,denom,i*denom)
           s.append(a)
           money=money-(i*denom)           
    return(s) 
change(1500)      
