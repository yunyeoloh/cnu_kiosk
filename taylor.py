#NR_taylor 풀이법
import numpy

def e(x,n,r=0):                                     #taylor급수 표현
    for k in range(n):
        r+= ((-1)**k)*(x**(2*k+1))/fac(2*k +1)
    return r
def ee(x,n,r = 0):                                     #taylor급수를 미분한 함수를 표현
    for k in range(n):
        r+= ((-1)**k)*(x**(2*k))/fac(2*k)
    return r

def fac(n): # n!를 구하는 fac함수를 구현
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

def nr(fcns,  fcnsp, a,b, tolv,count = 0):          #nr함수를 인자를 2개 받게 하여 taylor급수를 표현하기 좋게 변형
    while 1:
        if fcnsp(a,b) == 0:
            return "nr 실패"
        k = fcns(a,b)/fcnsp(a,b)
        a -= (fcns(a,b)/fcnsp(a,b))
        if a == 0:
            return f'ZeroDivision! {count}번 반복할 때에 해를 구했습니다.'
        if abs(k/a) < tolv:
            return f'{count}번 반복하여 얻은 x값은 {a}입니다. 오차는 {numpy.pi - a}입니다.'

            break

        else:
            count+=1

print(nr(e,ee,3.2,3,10**(-10)))
print(nr(e,ee,3.2,5,10**(-10)))
print(nr(e,ee,3.2,7,10**(-10)))
print(nr(e,ee,3.2,9,10**(-10)))
