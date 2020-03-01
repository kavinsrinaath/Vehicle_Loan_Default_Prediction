def dateconvert(val,delim):
    a = list(map(int,val.split(delim)))
    if a[2]<20:
        a[2] = a[2]+2000
    else:
        a[2] = a[2]+1900
    a = list(map(str,a))
    a = '-'.join(a)
    return a

def yrscalc(val):
    val = val.split()
    val[0] = val[0].replace('yrs','')
    val[1] = val[1].replace('mon','')
    val = list(map(int,val))
    yrs = round(((val[0]*12)+val[1])/12,2)
    return yrs