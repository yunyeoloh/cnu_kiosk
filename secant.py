#secant풀이법
def rootFinds_Secant(fcns,  a0, a1, tolv,count = 0):
    while 1:
        if fcns(a1) - fcns(a0) ==0 :
            return "secant 실패" ,"반복횟수" , count                    #분모가 0이 되어 나올 수 있는 오류를 막았습니다.
        k = fcns(a1) * (a1 - a0) / (fcns(a1) - fcns(a0))
        a0,a1 = a1,a1 - fcns(a1) * (a1 - a0) / (fcns(a1) - fcns(a0))
        if abs(k/a1) < tolv:                                         #오차값이 tolv값보다 작을 때 반복횟수 반환
            print(f'secant 풀이법 : {count}번 반복하여 얻은 x값은 {a1}입니다.')
            break
        else:
            count+=1
    return a1