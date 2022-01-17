## 1 задача
class time_is_negative (BaseException):
    pass
def decorator(yskor):
    def wrapper(v,v0,t):
        yskor(v,v0,t)
        s=v0*t+yskor(v,v0,t)*t**2/2
        return s
    return wrapper
@decorator
def yskor(v,v0,t):
    a= (v-v0)/t
    return a
try:
    v=int(input())
    v0=int(input())
    t=int(input())
    if t<=0:
        raise time_is_negative
except time_is_negative as time_is_negative:
    while t<=0:
        t=int(input())
        print('Время не может быть отрицательным.')

else:
    yskor(v,v0,t)

