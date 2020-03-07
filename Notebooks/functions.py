import pendulum

def dateconvert(val,delim):
    a = list(map(int,val.split(delim)))
    if a[2]<20:
        a[2] = a[2]+2000
    else:
        a[2] = a[2]+1900
    a = list(map(str,a))
    a = a[1]+'-'+a[0]+'-'+a[2]
    a = pendulum.parse(a,strict=False)
    return a

#custom function to convert string value to float
def yrscalc(val):
    val = val.split()
    val[0] = val[0].replace('yrs','')
    val[1] = val[1].replace('mon','')
    val = list(map(int,val))
    yrs = round(((val[0]*12)+val[1])/12,2)
    return yrs


#Get difference between 2 pendulum datetime objects in months
#returns a float value. eg: 2.11 means 2 yrs and 11 months
def time_diff_months(val):
    now = pendulum.now('UTC')
    t = now.diff(val).in_months()
    p = divmod(t,12) # Get quotient and remainder
    #combaining both values and coverting to string
    s = str(p[0])+'.'+str(p[1])
    s = float(s)
    return s