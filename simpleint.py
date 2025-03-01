"""
def simpleinterest(p,t,r):
    si=(p*t*r)/100
    print("simple interest is ",si)
    return si 


simpleinterest(10000,1,5)
"""
#compound interest 
def com_interest (p,t,r):
    a=p*(pow((1+r/1000),t))
    ci=a-p
    print("coumpound interest is ",ci)

com_interest(10000,1,5)
