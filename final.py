from fractions import Fraction as frac



# For Bayesian Network 1
# Return the result and pathverdict that answers this question:
# is ['B'] conditionally independent of ['A'] given ['C']?
#B II A | C
def question1():
    result = False
    pathverdict = [(('B', 'C', 'A'), False)]
    return result, pathverdict


# For Bayesian Network 1
# Return P(B,D,E) 
def question2(B, D, E, bn):
    PB = bn.B(value=B)
    PA0 = bn.A(value = 0)
    PA1 = bn.A(value = 1)
    PCBA00 = bn.C(value = 0, A = 0, B = B)
    PCBA01 = bn.C(value = 0, A = 1, B = B)
    PCBA10 = bn.C(value = 1, A = 0, B = B)
    PCBA11 = bn.C(value = 1, A = 1, B = B)
    PDC0 = bn.D(value = D, C = 0)
    PDC1 = bn.D(value = D, C = 1)
    PEC0 = bn.E(value = E, C = 0)
    PEC1 = bn.E(value = E, C = 1)
    ans = PB*PA0*PCBA00*PDC0*PEC0+PB*PA0*PCBA10*PDC1*PEC1
    ans = ans + PB*PA1*PCBA01*PDC0*PEC0+PB*PA1*PCBA11*PDC1*PEC1
    return ans


# For Bayesian Network 2
# Return the result and pathverdict that answers this question:
# is ['k'] independent of ['b']?
# K I B
def question3():
    result = False
    pathverdict = [(('k', 'g', 'e', 'f', 'd', 'b'), True), (('k', 'g', 'e', 'c', 'b'), False), (('k', 'g', 'e', 'c', 'a', 'd', 'b'), True), (('k', 'g', 'e', 'f', 'd', 'a', 'c', 'b'), True)]
    return result, pathverdict


# For Bayesian Network 2
# Return the result and pathverdict that answers this question:
# is ['a'] conditionally independent of ['h'] given ['f']?
# A I H \ f
def question4():
    result = True
    pathverdict = [(('a', 'd', 'f', 'h'), True), (('a', 'c', 'e', 'f', 'h'), True), (('a', 'c', 'b', 'd', 'f', 'h'), True)]
    return result, pathverdict


# For Bayesian Network 3
# Return the result and pathverdict that answers this question:
# is ['d'] independent of ['m']?
def question5():
    result = True
    pathverdict = [(('d', 'h', 'n', 'k', 'p', 'm'), True), (('d', 'h', 'n', 'k', 'e', 'c', 'f', 'm'), True), (('d', 'b', 'e', 'k', 'p', 'm'), True), (('d', 'b', 'e', 'c', 'f', 'm'), True)]
    return result, pathverdict


# For Bayesian Network 3
# Return the result and pathverdict that answers this question:
# is ['h'] conditionally independent of ['m'] given ['b', 'n']?
def question6():
    result = False
    pathverdict = [(('h', 'n', 'k', 'p', 'm'), True), (('h', 'n', 'k', 'e', 'c', 'f', 'm'), False), (('h', 'd', 'b', 'e', 'k', 'p', 'm'), True), (('h', 'd', 'b', 'e', 'c', 'f', 'm'), True)]
    return result, pathverdict


# For Bayesian Network 4
# Return P(c,d) 
def question7(c, d, bn):
    A0 = bn.a(value = 0)
    A1 = bn.a(value = 1)

    B00 = bn.b(value = 0, a = 0)
    B01 = bn.b(value = 0, a = 1)
    B10 = bn.b(value = 1, a = 0)
    B11 = bn.b(value = 1, a = 1)

    C00 = bn.c(value = c, b = 0, a = 0)
    C01 = bn.c(value = c, b = 0, a = 1)
    C10 = bn.c(value = c, b = 1, a = 0)
    C11 = bn.c(value = c, b = 1, a = 1)

    D = bn.d(value = d, c = c)

    ans = A0*B00*C00*D + A1*B01*C01*D + A0*B10*C10*D + A1*B11*C11*D
    return ans


# For Bayesian Network 4
# Return P(b,d | c) 
def question8(b, d, c, bn):
    A0 = bn.a(value = 0)
    A1 = bn.a(value = 1)

    B00 = bn.b(value = 0, a = 0)
    B01 = bn.b(value = 0, a = 1)
    B10 = bn.b(value = 1, a = 0)
    B11 = bn.b(value = 1, a = 1)

    B0 = bn.b(value = b, a = 0)
    B1 = bn.b(value = b, a = 1)

    C00 = bn.c(value = c, b = 0, a = 0)
    C01 = bn.c(value = c, b = 0, a = 1)
    C10 = bn.c(value = c, b = 1, a = 0)
    C11 = bn.c(value = c, b = 1, a = 1)

    CB0 = bn.c(value = c, b = b, a = 0)
    CB1 = bn.c(value = c, b = b, a = 1)

    D = bn.d(value = d, c = c)

    ansT = A0*B0*CB0*D + A1*B1*CB1*D
    ansB = A0*B00*C00 + A1*B01*C01 + A0*B10*C10 + A1*B11*C11
    return ansT*(1/ansB)


# For Bayesian Network 5
# Return P(a,c,e) 
def question9(a, c, e, bn):
    A = bn.a(value = a)

    B0 = bn.b(value = 0)
    B1 = bn.b(value = 1)

    C = bn.c(value = c, a = a)

    E0 = bn.e(value = e, b = 0, c = c)
    E1 = bn.e(value = e, b = 1, c = c)

    ans = A*C*B0*E0 + A*C*B1*E1
    return ans


# For Bayesian Network 5
# Return P(b,c,e | a,d) 
def question10(b, c, e, a, d, bn):
    A = bn.a(value = a)

    B= bn.b(value = b)

    B0 = bn.b(value = 0)
    B1 = bn.b(value = 1)

    C = bn.c(value = c, a = a)

    D = bn.d(value = d, a = a, b = b)

    D0 = bn.d(value = d, a = a, b = 0)
    D1 = bn.d(value = d, a = a, b = 1)

    E = bn.e(value = e, b = b, c = c)

    ansT = A*B*C*D*E
    ansB = A*B0*D0 + A*B1*D1

    return ansT*(1/ansB)