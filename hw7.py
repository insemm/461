from fractions import Fraction as frac
def question1Part1():
    result = False
    pathverdict = [(('a', 'b', 'd'), True),(('a', 'e', 'f', 'g', 'c', 'd'), False), (('a', 'e', 'd'), False)]
    return result,pathverdict

def question1Part2():
    result = False
    pathverdict = [(('a', 'b', 'd', 'c', 'g'), False), (('a', 'e', 'f', 'g'), True), (('a', 'e', 'd', 'c', 'g'), True), (('a', 'b', 'd', 'e', 'f', 'g'), True)]
    return result,pathverdict

def question1Part3():
    result = False
    pathverdict = [(('a', 'b', 'd', 'c', 'g'), False), (('a', 'e', 'f', 'g'), True), (('a', 'e', 'd', 'c', 'g'), False), (('a', 'b', 'd', 'e', 'f', 'g'), True)]
    return result,pathverdict

def question1Part4():
    result = False
    pathverdict = [(('a', 'b', 'd', 'c', 'g'), True), (('a', 'e', 'f', 'g'), False), (('a', 'e', 'd', 'c', 'g'), True), (('a', 'b', 'd', 'e', 'f', 'g'), True)]
    return result,pathverdict

def question2Part1():
    result = True
    pathverdict = [(('a', 'b', 'c', 'd'), True), (('a', 'b', 'e', 'f', 'g', 'd'), True)]
    return result,pathverdict

def question2Part2():
    result = False
    pathverdict = [(('a', 'b', 'c', 'd'), False), (('a', 'b', 'e', 'f', 'g', 'd'), False)]
    return result,pathverdict

def question2Part3():
    result = True
    pathverdict = [(('b', 'c', 'd', 'g'), True), (('b', 'e', 'f', 'g'), True)]
    return result,pathverdict

def question3Part1(a,b,c,d, bn):
    ap = bn.a(value = a)
    bp = bn.b(value = b)
    cp = bn.c(value = c, a = a, b = b)
    dp = bn.d(value = d, c = c)
    return ap*bp*cp*dp

def question3Part2(a,b,c, bn):
    ap = bn.a(value = a)
    bp = bn.b(value = b)
    cp = bn.c(value = c, a = a, b = b)
    return ap*bp*cp

def question3Part3(d, bn):
    dp1 = bn.d(value = d, c = 1) * (bn.c(value = 1, a = 0, b = 0)*bn.a(value = 0)*bn.b(value = 0) + bn.c(value = 1, a = 1, b = 0)*bn.a(value = 1)*bn.b(value = 0) + bn.c(value = 1, a = 0, b = 1)*bn.a(value = 0)*bn.b(value = 1) + bn.c(value = 1, a = 1, b = 1)*bn.a(value = 1)*bn.b(value = 1))
    dp2 = bn.d(value = d, c = 0) * (bn.c(value = 0, a = 0, b = 0)*bn.a(value = 0)*bn.b(value = 0) + bn.c(value = 0, a = 1, b = 0)*bn.a(value = 1)*bn.b(value = 0) + bn.c(value = 0, a = 0, b = 1)*bn.a(value = 0)*bn.b(value = 1) + bn.c(value = 0, a = 1, b = 1)*bn.a(value = 1)*bn.b(value = 1))
    return dp1+dp2

def question3Part4(a,b,c, bn):
    ap = bn.a(value = a)
    bp = bn.b(value = b)
    cp = bn.c(value = c, a = a, b = b)
    bt = 1/(bn.c(value = c, a = 0, b = 0)*bn.a(value = 0)*bn.b(value = 0) + bn.c(value = c, a = 1, b = 0)*bn.a(value = 1)*bn.b(value = 0) + bn.c(value = c, a = 0, b = 1)*bn.a(value = 0)*bn.b(value = 1) + bn.c(value = c, a = 1, b = 1)*bn.a(value = 1)*bn.b(value = 1))
    return ap*bp*cp*bt

def question3Part5(c, d, bn):
    cp = bn.c(value = c, a = 0, b = 0)*bn.a(value = 0)*bn.b(value = 0) * bn.c(value = c, a = 1, b = 0)*bn.a(value = 1)*bn.b(value = 0) * bn.c(value = c, a = 0, b = 1)*bn.a(value = 0)*bn.b(value = 1) * bn.c(value = c, a = 1, b = 1)*bn.a(value = 1)*bn.b(value = 1)
    dgc = bn.d(value = d, c = c)
    dp = question3Part3(d, bn)

    return dgc*cp*(1/dp)
 
def question4Part1(b,c,d, bn):
    bp = bn.a(value = 1)*bn.b(value = b, a = 1) + bn.a(value = 0)*bn.b(value = b, a = 0)
    cp = bn.a(value = 1)*bn.c(value = c, a = 1) + bn.a(value = 0)*bn.c(value = c, a = 0)
    return bp*cp*bn.d(value = d, b = b, c= c)

def question4Part2(c, d, bn):
    cp = bn.a(value = 1)*bn.c(value = c, a = 1) + bn.a(value = 0)*bn.c(value = c, a = 0)
    bp0 = bn.a(value = 1)*bn.b(value = 0, a = 1) + bn.a(value = 0)*bn.b(value = 0, a = 0)
    bp1 = bn.a(value = 1)*bn.b(value = 1, a = 1) + bn.a(value = 0)*bn.b(value = 1, a = 0)
    temp = bp0*cp*bn.d(value = d, c=c, b=0) + bp1*cp*bn.d(value = d, c=c, b=1)
    return temp*(1/cp)

def question4Part3(d, e, bn):
    cp0 = bn.a(value = 1)*bn.c(value = 0, a = 1) + bn.a(value = 0)*bn.c(value = 0, a = 0)
    cp1 = bn.a(value = 1)*bn.c(value = 1, a = 1) + bn.a(value = 0)*bn.c(value = 1, a = 0)
    bp0 = bn.a(value = 1)*bn.b(value = 0, a = 1) + bn.a(value = 0)*bn.b(value = 0, a = 0)
    bp1 = bn.a(value = 1)*bn.b(value = 1, a = 1) + bn.a(value = 0)*bn.b(value = 1, a = 0)
    dp = bn.d(value = d, c = 0, b = 0)*cp0*bp0 + bn.d(value = d, c = 0, b = 1)*cp0*bp1 + bn.d(value = d, c = 1, b = 0)*cp1*bp0 + bn.d(value = d, c = 1, b = 1)*cp1*bp1
    dp0 = bn.d(value = 0, c = 0, b = 0)*cp0*bp0 + bn.d(value = 0, c = 0, b = 1)*cp0*bp1 + bn.d(value = 0, c = 1, b = 0)*cp1*bp0 + bn.d(value = 0, c = 1, b = 1)*cp1*bp1
    dp1 = bn.d(value = 1, c = 0, b = 0)*cp0*bp0 + bn.d(value = 1, c = 0, b = 1)*cp0*bp1 + bn.d(value = 1, c = 1, b = 0)*cp1*bp0 + bn.d(value = 1, c = 1, b = 1)*cp1*bp1
    ep = dp0*bn.e(value = e, d = 0) + dp1*bn.e(value = e, d = 1)
    egd = bn.e(value = e, d = d)
    return egd*dp*(1/ep)
    


print(question1Part2())

def test():
    a1 = frac('169/1024')
    a0 = frac('855/1024')
    b10 = frac('33/64')
    b00 = frac('31/64')
    b11 = frac('247/512')
    b01 = frac('265/512')
    c10 = frac('585/1024')
    c11 = frac('535/1024')
    d00 = frac('75/256')
    d01 = frac('467/1024')
    d10 = frac('19/256')
    d11 = frac('361/1024')
    ans = b10*a0*c10*d11+b11*a1*c11*d11

    return ans

print(test())