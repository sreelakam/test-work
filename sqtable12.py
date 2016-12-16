def sq_tables(m):
    d=[]
    m=m+1
    for i in range(1,m):
        for j in range(1,m):
              d.append ('{:2}'.format(i*j)),
        d.append("\n")
    return d
